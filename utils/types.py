from typing import Tuple, Any, Iterable, TypeVar

T = TypeVar('T')

Solution = Tuple[Any, Any]

Position = Tuple[int, ...] # dims
Velocity = Tuple[int, ...]
Range = Tuple[int, int]
Matrix = Iterable[Iterable[T]]