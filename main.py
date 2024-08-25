from fasthtml.common import (
    Link,
    Div,
    Header,
    Nav,
    Ul,
    Li,
    A,
    Section,
    H1,
    H2,
    H3,
    H4,
    Img,
    fast_app,
    Title,
    serve,
    Article,
    Span,
    I,
)

app, rt = fast_app(
    pico=False,
    hdrs=(Link(rel="stylesheet", href="assets/css/main.css", type="text/css"),),
)


@app.get("/")
def home():
    header = Header(
        Div(
            H1("Portafolio Anthonyy", cls="h1"),
            Nav(
                Ul(
                    Li(
                        A("Inicio", href="#main"),
                    ),
                    Li(
                        A("Habilidades", href="#skill"),
                    ),
                    Li(
                        A("Proyectos", href="#project"),
                    ),
                )
            ),
            cls="contenedor-barra",
        )
    )
    section_social_networks = Section(
        Div(
            H1("Hola Mundo"),
        ),
        Div(
            H2("Vicente Antonio Gallegos Palafox"),
        ),
        H3("""Hola, soy un programador junior que le apasiona la tecnología y estoy
        estudiando "Ténologías de la información y desarrollo multiplataforma". Me
        especializo en desarrollo back-end en python."""),
        Div(
            A(
                Img(src="assets/img/gmail.png", alt="Gmail"),
                href="https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcSKjshvnGCDvrmhHrfHcNTZxPgSHsQmwtBhGsBsftBljzdxDrxKgMRVJnTvVBCsHDzqSDTlW",
                cls="color-a",
            ),
            A(
                Img(src="assets/img/github.png", alt="GitHub"),
                href="https://github.com/HaaruuKI",
                cls="color-a",
            ),
            A(
                Img(src="assets/img/linkedin.png"),
                href="https://www.linkedin.com/",
                cls="color-a",
            ),
            cls="redes-sociales",
        ),
        cls="section-main",
        id="main",
    )
    section_skill = Section(
        Div(
            H2("Habilidades de Tecnicas"),
            Ul(
                H4("Lenguajes de programacion"),
                Li("Python"),
                Li("C#"),
                Li("Bash"),
                H4("Frameworks"),
                Li("Django"),
                Li("FastHTML"),
                H4("Base de datos"),
                Li("MySql"),
                Li("Firebase"),
                Li("SQLITE3"),
                H4("Entorno de trabajo"),
                Li("GNU/Linux"),
            ),
        ),
        cls="section-main",
        id="skill",
    )
    section_project = Section(
        Div(
            Article(
                Div(
                    A(
                        Div(
                            cls="preview-image",
                        ),
                        href="#",
                        cls="preview--container",
                    ),
                    Div(cls="meta--container"),
                    cls="preview--container",
                ),
                Div(
                    Div(
                        A(
                            cls="title--text",
                        ),
                        cls="title--container",
                    ),
                    Div(
                        Ul(
                            Li(
                                A("Django", cls="tag"),
                            ),
                            Li(
                                A("Python", cls="tag"),
                            ),
                            Li(
                                A("HTML", cls="tag"),
                            ),
                            Li(
                                A("CSS", cls="tag"),
                            ),
                            Li(
                                A("JavaScript", cls="tag"),
                            ),
                            cls="tags--container",
                        ),
                        cls="tags--overflow-container",
                    ),
                    Div(
                        A(
                            Span(
                                I(
                                    "Repositorio",
                                    cls="fad fa-books",
                                ),
                                cls="icon-title",
                            ),
                            href="https://github.com/HaaruuKI/OasisVirtualNew",
                            cls="series button",
                        ),
                        A(
                            Span(
                                I(
                                    "Pagina",
                                    cls="far fa-image",
                                ),
                                cls="icon-title",
                            ),
                            Span(
                                I(
                                    cls="fas fa-arrow-circle-right",
                                ),
                                cls="new-tab",
                            ),
                            href="#",
                            cls="latest button",
                        ),
                        cls="hover--options",
                    ),
                    cls="content--container",
                ),
                cls="grid--item",
            ),
            cls="grid--cell",
        ),
        cls="grid--container",
        id="project",
    )
    return (
        Title("Hola"),
        header,
        section_social_networks,
        section_skill,
        section_project,
    )


serve()
