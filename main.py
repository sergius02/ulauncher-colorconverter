import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
import converter

logger = logging.getLogger(__name__)


class HexCodeExtension(Extension):

    def __init__(self):
        super(HexCodeExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def hexadecimal(self, text):
        hexadecimal = converter.normalize_hexadecimal(text)
        rgb = converter.hex_to_rgb(hexadecimal)
        hsv = converter.rgb_to_hsv(rgb)
        hsl = converter.hsv_to_hsl(hsv)

        return self.return_results(hexadecimal, rgb, hsv, hsl)

    def rgb(self, text):
        rgb = converter.get_int_tuple(text)
        hexadecimal = converter.rgb_to_hex(rgb)
        hsv = converter.rgb_to_hsv(rgb)
        hsl = converter.hsv_to_hsl(hsv)

        return self.return_results(hexadecimal, rgb, hsv, hsl)

    def hsv(self, text):
        hsv = converter.get_float_tuple(text)
        rgb = converter.hsv_to_rgb(hsv)
        hexadecimal = converter.rgb_to_hex(rgb)
        hsl = converter.hsv_to_hsl(hsv)

        return self.return_results(hexadecimal, rgb, hsv, hsl)

    def hsl(self, text):
        hsl = converter.get_float_tuple(text)
        hsv = converter.hsl_to_hsv(hsl)
        rgb = converter.hsv_to_rgb(hsv)
        hexadecimal = converter.rgb_to_hex(rgb)

        return self.return_results(hexadecimal, rgb, hsv, hsl)

    def return_results(self, hexadecimal, rgb, hsv, hsl):
        return [
            ExtensionResultItem(
                icon='images/icon.png',
                name=hexadecimal,
                description='HEX FORMAT',
                on_enter=CopyToClipboardAction(hexadecimal)
            ),
            ExtensionResultItem(
                icon='images/icon.png',
                name=rgb.__str__(),
                description='RGB FORMAT',
                on_enter=CopyToClipboardAction(rgb.__str__())
            ),
            ExtensionResultItem(
                icon='images/icon.png',
                name=hsv.__str__(),
                description='HSV FORMAT',
                on_enter=CopyToClipboardAction(hsv.__str__())
            ),
            ExtensionResultItem(
                icon='images/icon.png',
                name=hsl.__str__(),
                description='HSL FORMAT',
                on_enter=CopyToClipboardAction(hsl.__str__())
            )
        ]


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        text = event.get_argument() or ""
        if event.get_keyword() == "hex":
            return RenderResultListAction(extension.hexadecimal(text))

        if event.get_keyword() == "rgb":
            return RenderResultListAction(extension.rgb(text))

        if event.get_keyword() == "hsv":
            return RenderResultListAction(extension.hsv(text))

        if event.get_keyword() == "hsl":
            return RenderResultListAction(extension.hsl(text))

        return RenderResultListAction(items)


if __name__ == '__main__':
    HexCodeExtension().run()
