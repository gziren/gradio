"""gr.Button() component."""

from __future__ import annotations

from typing import Callable, Literal

from gradio_client.documentation import document, set_documentation_group
from gradio_client.serializing import StringSerializable

from gradio.blocks import Default, get
from gradio.components.base import IOComponent
from gradio.deprecation import warn_deprecation, warn_style_method_deprecation
from gradio.events import Clickable

set_documentation_group("component")


@document()
class Button(Clickable, IOComponent, StringSerializable):
    """
    Used to create a button, that can be assigned arbitrary click() events. The label (value) of the button can be used as an input or set via the output of a function.

    Preprocessing: passes the button value as a {str} into the function
    Postprocessing: expects a {str} to be returned from a function, which is set as the label of the button
    Demos: blocks_inputs, blocks_kinematics
    """

    def __init__(
        self,
        value: str | Callable | None | Default = Default("Run"),
        *,
        variant: Literal["primary", "secondary", "stop"]
        | Default = Default("secondary"),
        size: Literal["sm", "lg"] | Default = Default(None),
        visible: bool | Default = Default(True),
        interactive: bool | None | Default = Default(True),
        elem_id: str | None | Default = Default(None),
        elem_classes: list[str] | str | None | Default = Default(None),
        scale: int | None | Default = Default(None),
        min_width: int | Default = Default(160),
        **kwargs,
    ):
        """
        Parameters:
            value: Default text for the button to display. If callable, the function will be called whenever the app loads to set the initial value of the component.
            variant: 'primary' for main call-to-action, 'secondary' for a more subdued style, 'stop' for a stop button.
            size: Size of the button. Can be "sm" or "lg".
            visible: If False, component will be hidden.
            interactive: If False, the Button will be in a disabled state.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            scale: relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
        """
        self.variant = get(variant)
        if self.variant == "plain":
            warn_deprecation("'plain' variant deprecated, using 'secondary' instead.")
            self.variant = "secondary"
        self.size = get(size)

        IOComponent.__init__(
            self,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            interactive=interactive,
            scale=scale,
            min_width=min_width,
            **kwargs,
        )

    def style(
        self,
        *,
        full_width: bool | None = None,
        size: Literal["sm", "lg"] | None = None,
        **kwargs,
    ):
        """
        This method is deprecated. Please set these arguments in the constructor instead.
        """
        warn_style_method_deprecation()
        if full_width is not None:
            warn_deprecation(
                "Use `scale` in place of full_width in the constructor. "
                "scale=1 will make the button expand, whereas 0 will not."
            )
            self.scale = 1 if full_width else None
        if size is not None:
            self.size = size
        return self
