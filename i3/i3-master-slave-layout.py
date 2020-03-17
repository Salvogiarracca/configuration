#!/bin/python
import i3ipc

WORKSPACES = ['2 - Chrome',
              '3 - Dev']
WINDOW_CLASS_ALLOWED = ['st-256color']
THRESHOLD = 0.33


def resize_window(self, pct: str):
    self.command("resize shrink width %s px or %s ppt" % (pct, pct))


def callback_fun(self: i3ipc.Connection, event: i3ipc.WindowEvent):
    focused = i3.get_tree().find_focused()
    workspace_width = focused.workspace().rect.width
    workspace_height = focused.workspace().rect.height
    focused_width = focused.rect.width
    focused_height = focused.rect.height

    # The window has to be resized only if:
    #   - The workspace is in the workspaces list
    #   - The window is in the allowed list
    #   - The window height is near 100% of the workspace
    #   - The window width is more than the 33% of the screen
    if focused.workspace().name in WORKSPACES and \
            focused.window_class in WINDOW_CLASS_ALLOWED and \
            float(focused_height / workspace_height) > 0.95 and \
            float(focused_width / workspace_width) > THRESHOLD:

        if focused.workspace().layout == 'splith':
            self.command('split v')

        # Resize focused window to occupy only 1/3 of workspace (50% - 33% = 17%)
        resize_window(self, "17")


if __name__ == '__main__':
    i3 = i3ipc.Connection()
    i3.on('window::new', callback_fun)
    i3.main()
