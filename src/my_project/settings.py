from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    """
    Access your app's settings from this class.

    Example:
    ```python
    # a_secret_int: int
    # my_secret_str: SecretStr
    ```

    Usage:
    ```python
    from settings import Settings

    my_function(Settings.my_secret_str.get_secret_value())
    ```

    https://docs.pydantic.dev/latest/concepts/pydantic_settings/
    """


# https://github.com/pydantic/pydantic/issues/3753#issuecomment-1087417884
Settings = _Settings.model_validate({})
