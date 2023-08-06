"""Functions for converting between a mini-batch and micro-batches."""
from typing import List, Tuple, Union

import torch
from torch import Tensor
import torch.cuda.comm

__all__: List[str] = []


Tensors = Tuple[Tensor, ...]
TensorOrTensors = Union[Tensor, Tensors]
ChunkedTensorOrTensors = Union[List[Tensor], List[Tensors]]


def check(input: TensorOrTensors) -> None:
    """Checks whether the input is a tensor or tensors.

    Raises:
        TypeError: input is not a tensor or tensors.

    """
    if isinstance(input, tuple):
        for x in input:
            check(x)
        return

    if not isinstance(input, Tensor):
        raise TypeError('expected Tensor, but got %s' % input.__class__.__name__)


def scatter(input: TensorOrTensors, chunks: int, device: torch.device) -> ChunkedTensorOrTensors:
    """Splits an input mini-batch into multiple micro-batches."""
    if isinstance(input, tuple):
        buf = [scatter_1(x, chunks, device) for x in input]
        return list(zip(*buf))

    return scatter_1(input, chunks, device)


def scatter_1(tensor: Tensor, chunks: int, device: torch.device) -> List[Tensor]:
    """Choose the best PyTorch API for :func:`scatter`."""
    if not isinstance(tensor, Tensor):
        raise TypeError('expected Tensor to scatter, but got %s' % tensor.__class__.__name__)

    if device.type == 'cpu':
        tensor = tensor.to(device)
        return list(torch.chunk(tensor, chunks))

    device_id = device.index
    if device_id is None:
        device_id = torch.cuda.current_device()
    return list(torch.cuda.comm.scatter(tensor, [device_id] * chunks))


def gather(outputs: ChunkedTensorOrTensors, device: torch.device) -> TensorOrTensors:
    """Concatenates output micro-batches into a mini-batch."""
    if isinstance(outputs[0], tuple):
        buf = [gather_1(list(chunks), device) for chunks in zip(*outputs)]
        return tuple(buf)

    # NOTE(sublee): mypy could not infer the type after the above isinstance.
    return gather_1(outputs, device)  # type: ignore


def gather_1(tensors: List[Tensor], device: torch.device) -> Tensor:
    """Choose the best PyTorch API for :func:`gather`."""
    if device.type == 'cpu':
        tensor = torch.cat(tensors)
        return tensor.to(device)

    device_id = device.index
    if device_id is None:
        device_id = torch.cuda.current_device()
    return torch.cuda.comm.gather(tensors, destination=device_id)
