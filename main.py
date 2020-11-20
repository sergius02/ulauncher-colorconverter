
import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)


class HexCodeExtension(Extension):

    def __init__(self):
        super(HexCodeExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

    def toRGB(self, text):
        hex = text.replace("#","")
        rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)).__str__()

        return [
                    ExtensionResultItem(
                        icon='images/icon.png',
                        name="#" + hex.upper(),
                        description='HEX FORMAT',
                        on_enter=CopyToClipboardAction("#" + hex.upper())
                    ),
                    ExtensionResultItem(
                        icon='images/icon.png',
                        name=rgb.__str__(),
                        description='RGB FORMAT',
                        on_enter=CopyToClipboardAction(rgb.__str__())
                    )
                ]

    def toHex(self, text):
        rgb = text.replace("(","")
        rgb = rgb.replace(")","")
        rgb = rgb.replace(" ", "")

        rgbtuple = tuple(map(int, rgb.split(',')))

        hex = '%02x%02x%02x' % rgbtuple

        return [
                    ExtensionResultItem(
                        icon='images/icon.png',
                        name="#" + hex.upper(),
                        description='HEX FORMAT',
                        on_enter=CopyToClipboardAction("#" + hex.upper())
                    ),
                    ExtensionResultItem(
                        icon='images/icon.png',
                        name=rgb,
                        description='RGB FORMAT',
                        on_enter=CopyToClipboardAction(rgb)
                    )
                ]


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        text = event.get_argument() or ""
        if event.get_keyword() == "tohex":
            return RenderResultListAction(extension.toHex(text))
        
        if event.get_keyword() == "torgb":
            return RenderResultListAction(extension.toRGB(text))

        return RenderResultListAction(items)

if __name__ == '__main__':
    HexCodeExtension().run()
    
