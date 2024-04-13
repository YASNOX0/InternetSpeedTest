from time import sleep
from flet import *
import speedtest


def main(page: Page):

    # region Page Settings
    page.platform = PagePlatform.WINDOWS
    page.title = "Internet speed test"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.padding = 30
    page.bgcolor = colors.BLACK
    page.auto_scroll = True
    page.scroll = ScrollMode.HIDDEN

    page.fonts = {
        "RoosterPersonalUse": "fonts/RoosterPersonalUse-3z8d8.ttf",
        "SourceCodePro-BlackItalic": "fonts/SourceCodePro-BlackItalic.ttf",
        "SourceCodePro-Bold.ttf": "fonts/SourceCodePro-Bold.ttf"
    }
    # endregion

    # region Progressbar Sett
    pb_speedTest1 = ProgressBar(
        width=400,
        bgcolor=colors.CYAN_ACCENT_400,
        color="blue"
    )
    pb_speedTest2 = ProgressBar(
        width=400,
        bgcolor=colors.CYAN_ACCENT_400,
        color="blue"
    )
    ct_testProgress1 = Container(
        opacity=0,
        margin=margin.only(left=20),
        content=pb_speedTest1
    )
    ct_testProgress2 = Container(
        opacity=0,
        margin=margin.only(left=20),
        content=pb_speedTest2
    )
    # endregion

    # region Lines(Text) handle
    t_line1 = Text(
        value="> press start...",
        font_family="SourceCodePro-BlackItalic",
        color="white"
    )
    t_line2 = Text(
        value="",
        font_family="SourceCodePro-BlackItalic",
        color="green"
    )
    t_line3 = Text(
        value="",
        font_family="SourceCodePro-BlackItalic",
        color="green"
    )
    t_line4 = Text(
        value="",
        font_family="SourceCodePro-Bold.ttf",
        color="yellow"
    )
    t_line5 = Text(
        value="",
        font_family="SourceCodePro-BlackItalic",
        color="green"
    )
    t_line6 = Text(
        value="",
        font_family="SourceCodePro-BlackItalic",
        color="green"
    )
    t_line7 = Text(
        value="",
        font_family="SourceCodePro-Bold.ttf",
        color="yellow"
    )
    t_line8 = Text(
        value="",
        font_family="SourceCodePro-BlackItalic",
        color="white"
    )
    # endregion

    # region Internet speed test terminal handle
    speedContainer = Container(
        margin=margin.only(top=15, bottom=15),
        padding=35,
        width=250,
        height=100,
        border_radius=30,
        gradient=LinearGradient(
            begin=alignment.top_right,
            end=alignment.bottom_left,
            colors=[colors.BLUE, colors.BLUE_100],
        ),
        animate=animation.Animation(
            duration=1000,
            curve=AnimationCurve.EASE_OUT_BACK
        ),
        content=Column(
            controls=[
                t_line1,
                t_line2,
                t_line3,
                ct_testProgress1,
                t_line4,
                t_line5,
                t_line6,
                ct_testProgress2,
                t_line7,
                t_line8
            ]
        ),

    )
    # endregion

    # region Calculation internet speed
    st = speedtest.Speedtest()

    def showSpeedContainer(e):
        speedContainer.visible = True
        speedContainer.width = 1000
        speedContainer.height = 400
        t_line1.value = "> Calculating download speed, please wait..."
        speedContainer.update()
        sleep(0.75)

        idealServer = st.get_best_server()
        city = idealServer["name"]
        country = idealServer["country"]
        cc = idealServer["cc"]

        t_line2.value = f"> finding the best possible server in {city}, {country} ({cc})"
        speedContainer.update()
        sleep(1.5)

        t_line3.value = f"> connection established, status OK', fetching download speed, please wait..."
        ct_testProgress1.opacity = 1
        speedContainer.update()
        downloadSpeed = st.download() / 1024 / 1024
        pb_speedTest1.value = 1
        t_line4.value = f"> the download speed is {str(round(downloadSpeed, 2))} mbps"
        speedContainer.update()

        t_line5.value = f"> calculating the upload speed please wait"
        speedContainer.update()
        sleep(0.75)

        t_line6.value = "> executing upload script, hold on"
        ct_testProgress2.opacity = 1
        speedContainer.update()

        uploadSpeed = st.upload() / 1024 / 1024
        pb_speedTest2.value = 1
        t_line7.value = f"> the upload speed is {str(round(uploadSpeed, 2))} mbps"
        speedContainer.update()
        sleep(0.75)

        t_line8.value = ("> task completed successfully\n\n"
                         ">> App developer : SAADEN Yassin")
        speedContainer.update()
    # endregion

    page.add(
        Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Text(
                    value="Internet Speed",
                    font_family="RoosterPersonalUse",
                    style="displayLarge",
                    color="blue"
                ),
                Text(
                    value="Test",
                    font_family="RoosterPersonalUse",
                    size=25
                )
            ]
        ),
        speedContainer,
        IconButton(
            icon=icons.PLAY_CIRCLE_FILL_OUTLINED,
            icon_size=50,
            icon_color="blue",
            on_click=showSpeedContainer
        )
    )


app(target=main, assets_dir="assets")
