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
        cmyk = converter.rgb_to_cmyk(rgb)

        return self.return_results(hexadecimal, rgb, hsv, hsl, cmyk)

    def rgb(self, text):
        rgb = converter.get_int_tuple(text)

        hexadecimal = converter.rgb_to_hex(rgb)
        hsv = converter.rgb_to_hsv(rgb)
        hsl = converter.hsv_to_hsl(hsv)
        cmyk = converter.rgb_to_cmyk(rgb)

        return self.return_results(hexadecimal, rgb, hsv, hsl, cmyk)

    def hsv(self, text):
        hsv = converter.get_float_tuple(text)

        rgb = converter.hsv_to_rgb(hsv)
        hexadecimal = converter.rgb_to_hex(rgb)
        hsl = converter.hsv_to_hsl(hsv)
        cmyk = converter.rgb_to_cmyk(rgb)

        return self.return_results(hexadecimal, rgb, hsv, hsl, cmyk)

    def hsl(self, text):
        hsl = converter.get_float_tuple(text)

        hsv = converter.hsl_to_hsv(hsl)
        rgb = converter.hsv_to_rgb(hsv)
        hexadecimal = converter.rgb_to_hex(rgb)
        cmyk = converter.rgb_to_cmyk(rgb)

        return self.return_results(hexadecimal, rgb, hsv, hsl, cmyk)

    def cmyk(self, text):
        cmyk = converter.get_float_tuple(text)

        rgb = converter.cmyk_to_rgb(cmyk)
        hsv = converter.rgb_to_hsv(rgb)
        hsl = converter.hsv_to_hsl(hsv)
        hexadecimal = converter.rgb_to_hex(rgb)

        return self.return_results(hexadecimal, rgb, hsv, hsl, cmyk)

    @staticmethod
    def return_results(hexadecimal, rgb, hsv, hsl, cmyk):
        return [
            ExtensionResultItem(
                icon='images/icon.png',
                name=hexadecimal,
                description='HEX',
                on_enter=CopyToClipboardAction(hexadecimal)
            ),
            ExtensionResultItem(
                icon='images/icon.png',
                name=converter.normalize_rgb(rgb),
                description='RGB',
                on_enter=CopyToClipboardAction(converter.normalize_rgb(rgb))
            ),
            ExtensionResultItem(
                icon='images/icon.png',
                name=converter.normalize_hsl_hsv(hsv),
                description='HSV',
                on_enter=CopyToClipboardAction(converter.normalize_hsl_hsv(hsv))
            ),
            ExtensionResultItem(
                icon='images/icon.png',
                name=converter.normalize_hsl_hsv(hsl),
                description='HSL',
                on_enter=CopyToClipboardAction(converter.normalize_hsl_hsv(hsl))
            ),
            ExtensionResultItem(
                icon='images/icon.png',
                name=converter.normalize_cmyk(cmyk),
                description='CMYK',
                on_enter=CopyToClipboardAction(converter.normalize_cmyk(cmyk))
            )
        ]


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        text = event.get_argument() or ""
        if event.get_keyword() == extension.preferences.get("color_converter_hex"):
            return RenderResultListAction(extension.hexadecimal(text))

        if event.get_keyword() == extension.preferences.get("color_converter_rgb"):
            return RenderResultListAction(extension.rgb(text))

        if event.get_keyword() == extension.preferences.get("color_converter_hsv"):
            return RenderResultListAction(extension.hsv(text))

        if event.get_keyword() == extension.preferences.get("color_converter_hsl"):
            return RenderResultListAction(extension.hsl(text))

        if event.get_keyword() == extension.preferences.get("color_converter_cmyk"):
            return RenderResultListAction(extension.cmyk(text))

        return RenderResultListAction(items)


if __name__ == '__main__':
    HexCodeExtension().run()
