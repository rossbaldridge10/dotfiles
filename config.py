
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod1"    # mod1 = Alt    mod4 = Super
terminal = guess_terminal()

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    
    # Qtile system commands
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

####    ##### launchers
    Key([mod], "Return", lazy.spawn("alacritty"), 
        desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("vivaldi-stable"), 
        desc="Launch Vivaldi browser"),
    Key([mod], "r", lazy.spawn("dmenu_run"),
        desc="Spawn a command using a prompt widget"),
#    Key([mod], "r", extension.Dmenu(dmenu_bottom=True),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    #layout.Max(),
    #layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(),
    layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    margin=0,
    font='UbuntuMono Nerd Font Bold',
    fontsize=16,
    padding=0,
    background='000000',
    foreground='ffffff'
)
extension_defaults = widget_defaults.copy()
#################################################################################
blue='104d84'
lblue='4e77b5'
green='336b28'
lgreen='77b54e'
black='000000'
white='ffffff'

screens = [
    Screen(
       top =bar.Bar(
            [
                widget.TextBox(foreground=black,background=green,text='',fontsize=48,padding=-3), # textbox
                #widget.CurrentLayout(background=green), # currentLayout
                widget.CurrentLayoutIcon(background=green,padding=7), # currentLayoutIcon
                widget.TextBox(foreground=green,background=blue,text='',fontsize=48,padding=-3), # textbox
                widget.GroupBox(visible_groups='123456789',background=blue,inactive=lblue,active=lgreen,
                    this_current_screen_border='c0c0c0'), # groupBox
                widget.TextBox(foreground=blue,text='',fontsize=48,padding=-3), # textbox
                widget.WindowName(padding=10), # windowName
                #widget.Chord(
                    #chords_colors={
                        #'launch': ("#ff0000", "#ffffff"),
                    #},
                    #name_transform=lambda name: name.upper(),
                #),
                #widget.Wlan(),
                widget.TextBox(text='',fontsize=48,background=black,foreground=blue,padding=-3),
                widget.TextBox(text=' ',fontsize=18,background=blue,foreground=white,padding=0),
                widget.Clock(format='%m-%d %I:%M',padding=5,background=blue), # clock
                widget.TextBox(text='',fontsize=48,foreground=green,background=blue,padding=-3),
                widget.BatteryIcon(background=green,padding=5),
#                widget.Battery(background=green,padding=5), # battery
                widget.TextBox(text='',fontsize=48,foreground=blue,background=green,padding=-3),
                widget.QuickExit(default_text='[X]',padding=7,background=blue), # quickExit
                widget.TextBox(text='',fontsize=48,foreground=black,background=blue,padding=-3),
                #widget.Systray()
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
