import asyncio
import functools
import time
from collections.abc import Callable, Coroutine
from typing import Any, overload

type _Coro[T] = Coroutine[Any, Any, T]
type _WrappedDeco[**P, T] = Callable[
    [Callable[P, _Coro[T]]],
    Callable[P, _Coro[T | None]],
]


@overload
def athrottle[**P, R](*, delay: float = 1) -> _WrappedDeco[P, R]: ...


@overload
def athrottle[**P, T](
    _func: Callable[P, _Coro[T]],
    *,
    delay: float = 1,
) -> Callable[P, _Coro[T | None]]: ...


def athrottle[**P, T](
    _func: Callable[P, _Coro[T]] | None = None,
    *,
    delay: float = 1,
) -> Callable[P, _Coro[T | None]] | _WrappedDeco[P, T]:
    """
    Throttle an async function.

    Returns `None` if called within window.

    `delay`: Minimum interval between invocations.

    Usage:

    ```python
    # Use default delay
    @athrottle
    async def my_func(): ...

    # Or specify a custom delay
    @athrottle(delay=3)
    async def my_func(): ...
    ```
    """

    def decorate(
        func: Callable[P, _Coro[T]],
    ) -> Callable[P, _Coro[T | None]]:
        last_called: float | None = None
        lock = asyncio.Lock()

        @functools.wraps(func)
        async def wrapped_async(*args: P.args, **kwargs: P.kwargs) -> T | None:
            # The lock is necessary to ensure that tasks created at the same time don't simultaneously modify last_called
            async with lock:
                nonlocal last_called
                now = time.time()
                result = None
                if not last_called or now - last_called > delay:
                    result = await func(*args, **kwargs)
                    last_called = now
            return result

        return wrapped_async

    if _func:
        # Decorator called without arguments: _func is passed
        # We apply and return the decorated function (with default values)
        return decorate(_func)
    # Decorator called with arguments: _func will be None
    # We return the decorator (as a closure), which will then be applied to the function
    return decorate
