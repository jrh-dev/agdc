


def centered_quote(text: str, height: int) -> str:
    """
    Center the quote in the middle of the container.
    """
    return f"""
    <style>
    P.center {{ text-align: center }}
    DIV.container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: {height}px;
    }}
    </style>
    <div class="container">
    <p class="center">{text}</p>
    </div>
    """

def custom_h1(text: str, size: int = 45) -> str:
    """
    Custom h1 style.
    """
    return f'<h1 align="center" style="font-size:{size}px"> {text} </h1>'