# Center tk window
A small library for centering tkinter windows on their parent or on the screen.

## Installation
To install run the following command:
`pip install center_tk_window`

## Usage
```python
import tkinter
import center_tk_window

root_window = tkinter.Tk()
window_to_center = tkinter.Toplevel(root_window)

# Center a window on its parent unless it is the root window in which case it will be centered on screen.
center_tk_window.center(root_window, window_to_center)

# Center a window on its parent
center_tk_window.center_on_parent(root_window, window_to_center)

# Center a window on the screen
center_tk_window.center_on_screen(window_to_center)

```
