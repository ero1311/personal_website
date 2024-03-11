import dash
import dash_mantine_components as dmc
from dash_iconify import DashIconify

app = dash.Dash(
    __name__,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ]
)

app.layout = dmc.MantineProvider(
    theme={
        "colorScheme": "dark",
        "colors": {
            "hacker": [
                "#20c20e",
                "#20c20e",
                "#20c20e",
                "#20c20e",
                "#20c20e",
                "#20c20e",
                "#20c20e",
                "#20c20e",
                "#20c20e",
                "#20c20e"
            ]
        },
        "primaryColor": "hacker",
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        dmc.Grid(
            children=[
                dmc.Col(
                    children=[
                        dmc.Grid(
                            children=[
                                dmc.Col(
                                    dmc.Card(
                                        children=[
                                            dmc.CardSection(
                                                dmc.Image(
                                                    src=dash.get_asset_url("imgs/erik_pic.jpg"),
                                                    height=240,
                                                )
                                            ),
                                            dmc.Group(
                                                [
                                                    dmc.Title(
                                                        "Erik Harutyunyan", 
                                                        order=3,
                                                        color="hacker"
                                                    ),
                                                ],
                                                position="apart",
                                                mt="md",
                                                mb="xs",
                                            ),
                                            dmc.Group(
                                                [
                                                    dmc.Anchor(
                                                        DashIconify(icon="ion:logo-github", width=25),
                                                        href="https://github.com/ero1311"
                                                    ),
                                                    dmc.Anchor(
                                                        DashIconify(icon="ion:logo-linkedin", width=25),
                                                        href="https://www.linkedin.com/in/erik-harutyunyan-293458131/"
                                                    ),
                                                    dmc.Anchor(
                                                        DashIconify(icon="ion:logo-facebook", width=25),
                                                        href="https://www.facebook.com/erik.h1311/"
                                                    ),
                                                    dmc.Anchor(
                                                        DashIconify(icon="ic:baseline-telegram", width=25),
                                                        href="https://t.me/ero1311/"
                                                    ),
                                                    dmc.Anchor(
                                                        DashIconify(icon="cib:toptal", width=25),
                                                        href="https://www.toptal.com/resume/erik-harutyunyan"
                                                    ),
                                                ],
                                                position="apart",
                                                mt="md",
                                                mb="xs",
                                            ),
                                        ],
                                        withBorder=True,
                                        shadow="sm",
                                        radius="md",
                                        pos="fixed"
                                    ),
                                    span=3
                                ),
                                dmc.Col(
                                    dmc.Stack(
                                        [
                                            dmc.Divider(
                                                label=dmc.Title("Education", order=3),
                                                labelPosition="center",
                                                orientation="horizontal",
                                                variant="solid",
                                                color="hacker"
                                            ),
                                            dmc.Paper(
                                                children=[
                                                    dmc.List(
                                                        [
                                                            dmc.ListItem(
                                                                dmc.SimpleGrid(
                                                                    children=[
                                                                        dmc.Text(
                                                                            [
                                                                                "2020-2022",
                                                                            ],
                                                                            color="hacker"
                                                                        ),
                                                                        dmc.Text(
                                                                            [
                                                                                "MS in Mathematics in Data Science",
                                                                            ],
                                                                            color="hacker"
                                                                        ),
                                                                        dmc.Text(
                                                                            [
                                                                                "@ Technische Universität München (TUM)",
                                                                            ],
                                                                            color="hacker"
                                                                        ),
                                                                    ],
                                                                    cols=3,
                                                                    spacing="xs"
                                                                ),
                                                            ),
                                                            dmc.ListItem(
                                                                dmc.SimpleGrid(
                                                                    children=[
                                                                        dmc.Text(
                                                                            [
                                                                                "2014-2018",
                                                                            ],
                                                                            color="hacker"
                                                                        ),
                                                                        dmc.Text(
                                                                            [
                                                                                "BS in Computer Science",
                                                                            ],
                                                                            color="hacker"
                                                                        ),
                                                                        dmc.Text(
                                                                            [
                                                                                "@ American University of Armenia (AUA)",
                                                                            ],
                                                                            color="hacker"
                                                                        ),
                                                                    ],
                                                                    cols=3,
                                                                    spacing="xs"
                                                                ),
                                                            ),
                                                        ],
                                                        icon=dmc.ThemeIcon(
                                                            DashIconify(icon="mdi:education-outline", width=16),
                                                            color="hacker",
                                                            variant="outline"
                                                        ),
                                                        spacing="xs"
                                                    )
                                                ],
                                                shadow="lg",
                                                radius="lg",
                                            ),
                                            dmc.Divider(
                                                label=dmc.Title("Work Experience", order=3),
                                                labelPosition="center",
                                                orientation="horizontal",
                                                variant="solid",
                                                color="hacker"
                                            ),
                                            dmc.Paper(
                                                children=[
                                                    dmc.List(
                                                        [
                                                            dmc.ListItem(
                                                                children=[
                                                                    dmc.SimpleGrid(
                                                                        children=[
                                                                            dmc.Text(
                                                                                [
                                                                                    "2023/07-Present",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "Lead of R&D",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "@ Manot",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                        ],
                                                                        cols=3,
                                                                        spacing="xs"
                                                                    ),
                                                                    dmc.List(
                                                                        [
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Design and implement ML models that analyze and pinpoints weaknesses of Computer Vision models"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Research on and experiment with new directions in which Manot's capabilites can be expanded"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Research on and experiment with new features requested by the customers"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Lead the development of Manot backend SaaS and on premise solutions"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dmc.ListItem(
                                                                children=[
                                                                    dmc.SimpleGrid(
                                                                        children=[
                                                                            dmc.Text(
                                                                                [
                                                                                    "2018/09-2023/02",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "Computer Vision Engineer",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "@ SuperAnnotate",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                        ],
                                                                        cols=3,
                                                                        spacing="xs"
                                                                    ),
                                                                    dmc.List(
                                                                        [
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Advised and shared expertise with LiDAR point cloud data, guiding the development of the LiDAR annotation tool"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Guided the video action recognition smart feature in the video editor tool"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Led the real-time object tracking smart feature in the video editor tool"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Proofread and commented on computer vision-related marketing articles and whitepapers"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Used state-of-the-art uncertainty estimation methods to develop the priority score feature for the tool that suggests to the annotator which images to annotate first"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Improved the speed of an edge detection model by around five times applying state-of-the-art knowledge distillation and channel pruning methods, with only losing 1% in the F1 score"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Researched and developed an improvement for the smart segmentation algorithm that lies in the core of the SuperAnnotate"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Employed OpenVINO and TensorRT to develop an integration covering from uploading raw data to the platform to training and subsequent deployment of object detection models to OAK-D and Jetson Nano devices, respectively"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Developed analytics and visualization functions for the SDK to give insights into raw data and its annotations"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Wrote medium articles and whitepapers about the cutting-edge projects done in SuperAnnotate"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dmc.ListItem(
                                                                children=[
                                                                    dmc.SimpleGrid(
                                                                        children=[
                                                                            dmc.Text(
                                                                                [
                                                                                    "2017/09-2018/09",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "Data Scientist",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "@ UCOM",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                        ],
                                                                        cols=3,
                                                                        spacing="xs"
                                                                    ),
                                                                    dmc.List(
                                                                        [
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Created an anomaly detection system using classical time series forecasting methods to predict the going down of internet spreading towers. The system helped to decrease the towers' downtime by four times on average"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Developed tabular customer data of the company to predict the churn of each customer. The model reached around 85% accuracy when deployed in production"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                            dmc.ListItem(
                                                                                dmc.Text(
                                                                                    [
                                                                                        "Used customer service usage data to provide a trustworthiness score that the company decided whether to sell mobile phones with monthly payments or demand the full price at once"
                                                                                    ],
                                                                                    color="hacker"
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ],
                                                        icon=dmc.ThemeIcon(
                                                            DashIconify(icon="material-symbols:work-outline", width=16),
                                                            color="hacker",
                                                            variant="outline"
                                                        ),
                                                        spacing="xs"
                                                    )
                                                ],
                                                shadow="lg",
                                                radius="lg",
                                            ),
                                            dmc.Divider(
                                                label=dmc.Title("Competitions and Awards", order=3),
                                                labelPosition="center",
                                                orientation="horizontal",
                                                variant="solid",
                                                color="hacker"
                                            ),
                                            dmc.Paper(
                                                children=[
                                                    dmc.List(
                                                        [
                                                            dmc.ListItem(
                                                                children=[
                                                                    dmc.SimpleGrid(
                                                                        children=[
                                                                            dmc.Text(
                                                                                [
                                                                                    "2021",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "CV3DST:MOT Challenge",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "@ Technische Universität München (TUM)",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                        ],
                                                                        cols=3,
                                                                        spacing="xs"
                                                                    ),
                                                                    dmc.Text(
                                                                        [
                                                                            'Took the first place in Multiple Object Tracking competition organized by "Computer Vision 3: Detection, Segmentation, Tracking" course on the MOT16 dataset'
                                                                        ],
                                                                        color="hacker"
                                                                    )
                                                                ]
                                                            ),
                                                            dmc.ListItem(
                                                                children=[
                                                                    dmc.SimpleGrid(
                                                                        children=[
                                                                            dmc.Text(
                                                                                [
                                                                                    "2017",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "ACM-ICPC",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                        ],
                                                                        cols=3,
                                                                        spacing="xs"
                                                                    ),
                                                                    dmc.Text(
                                                                        [
                                                                            'Won ACM-ICPC(university level programming competition) country phase and passed to regional phase which was held in Tbilisi, Georgia'
                                                                        ],
                                                                        color="hacker"
                                                                    )
                                                                ]
                                                            ),
                                                            dmc.ListItem(
                                                                children=[
                                                                    dmc.SimpleGrid(
                                                                        children=[
                                                                            dmc.Text(
                                                                                [
                                                                                    "2017",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "Republic of Armenia presidential award",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                        ],
                                                                        cols=3,
                                                                        spacing="xs"
                                                                    ),
                                                                    dmc.Text(
                                                                        [
                                                                            'I was awarded Republic of Armenia presidential award in best Bachelor student nomination'
                                                                        ],
                                                                        color="hacker"
                                                                    )
                                                                ]
                                                            ),
                                                            dmc.ListItem(
                                                                children=[
                                                                    dmc.SimpleGrid(
                                                                        children=[
                                                                            dmc.Text(
                                                                                [
                                                                                    "2015",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "IMC (International Mathematics Competition)",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                        ],
                                                                        cols=3,
                                                                        spacing="xs"
                                                                    ),
                                                                    dmc.Text(
                                                                        [
                                                                            'Participated in IMC(International Mathematics Competition) which was held in Blagoevgrad, Bulgaria. As an award received a certificate.'
                                                                        ],
                                                                        color="hacker"
                                                                    )
                                                                ]
                                                            ),
                                                            dmc.ListItem(
                                                                children=[
                                                                    dmc.SimpleGrid(
                                                                        children=[
                                                                            dmc.Text(
                                                                                [
                                                                                    "2015",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                            dmc.Text(
                                                                                [
                                                                                    "ACM-ICPC",
                                                                                ],
                                                                                color="hacker"
                                                                            ),
                                                                        ],
                                                                        cols=3,
                                                                        spacing="xs"
                                                                    ),
                                                                    dmc.Text(
                                                                        [
                                                                            'Won ACM-ICPC(university level programming competition) country phase and passed to regional phase which was held in Tbilisi, Georgia'
                                                                        ],
                                                                        color="hacker"
                                                                    )
                                                                ]
                                                            ),
                                                        ],
                                                        icon=dmc.ThemeIcon(
                                                            DashIconify(icon="healthicons:award-trophy-outline", width=16),
                                                            color="hacker",
                                                            variant="outline"
                                                        ),
                                                        spacing="xs"
                                                    )
                                                ],
                                                shadow="lg",
                                                radius="lg",
                                            ),
                                        ],
                                        spacing="md",
                                    ),
                                    span=9
                                )
                            ],
                            mt="xs"
                        )
                    ],
                    offset=2,
                    span=8
                )
            ]
        )
    ],
)


if __name__ == "__main__":
    app.run_server(debug=False, port=8051, use_reloader=True)