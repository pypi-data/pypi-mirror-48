"""A GPipe implementation in PyTorch."""
from torchgpipe.__version__ import __version__  # noqa
from torchgpipe.checkpoint import is_recomputing
from torchgpipe.gpipe import GPipe, current_microbatch

__all__ = ['GPipe', 'current_microbatch', 'is_recomputing']
