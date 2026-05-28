from flask import Flask, Response, render_template, send_from_directory

SERVICES: list[dict[str, str]] = [
    {
        "slug": "excavaciones-generales",
        "title": "Excavaciones generales",
        "description": (
            "Excavaciones de cualquier escala para obra civil, rural o "
            "residencial, con retroexcavadora preparada para terrenos exigentes."
        ),
    },
    {
        "slug": "zanjas-canerias",
        "title": "Zanjas para cañerías, agua y saneamiento",
        "description": (
            "Apertura precisa de zanjas para tendido de cañerías de agua, "
            "saneamiento y servicios subterráneos."
        ),
    },
    {
        "slug": "cimientos-plateas",
        "title": "Cimientos y plateas",
        "description": (
            "Preparación de bases, cimientos y plateas listas para hormigonado "
            "según los requerimientos de tu obra."
        ),
    },
    {
        "slug": "limpieza-terrenos",
        "title": "Limpieza de terrenos",
        "description": (
            "Desmonte, retiro de troncos, escombros y vegetación para dejar "
            "el terreno pronto para construir o cultivar."
        ),
    },
    {
        "slug": "nivelacion-rellenos",
        "title": "Nivelación y rellenos",
        "description": (
            "Movimiento de suelos, nivelación de predios y rellenos compactados "
            "para terrenos parejos y firmes."
        ),
    },
    {
        "slug": "accesos-caminos",
        "title": "Apertura de accesos y caminos",
        "description": (
            "Habilitación de accesos vehiculares, caminos rurales y entradas "
            "a campos y casas."
        ),
    },
    {
        "slug": "trabajos-rurales-urbanos",
        "title": "Trabajos rurales y urbanos",
        "description": (
            "Operamos tanto en zonas urbanas como rurales de Colonia, con la "
            "logística que cada lugar requiere."
        ),
    },
]

GALLERY_IMAGES: list[dict[str, str]] = [
    {"file": "01-barro-atardecer.jpg", "alt": "Retroexcavadora trabajando al atardecer"},
    {"file": "02-maquina-jcb.jpg", "alt": "Retroexcavadora JCB FF Retro"},
    {"file": "04-pala-cargada.jpg", "alt": "Pala frontal cargada"},
    {"file": "05-limpieza-tocon.jpg", "alt": "Limpieza de terreno y extracción de tocón"},
    {"file": "06-trabajo-noche.jpg", "alt": "Retroexcavadora trabajando de noche"},
    {"file": "07-pov-cabina.jpg", "alt": "Vista desde la cabina"},
    {"file": "09-jcb-palmera.jpg", "alt": "Retroexcavadora en obra junto a una palmera"},
    {"file": "10-nivelacion.jpg", "alt": "Nivelación de terreno"},
    {"file": "11-zanja-canerias.jpg", "alt": "Apertura de zanja para cañerías"},
    {"file": "12-acceso-casa.jpg", "alt": "Apertura de acceso a vivienda"},
    {"file": "13-noche-neon.jpg", "alt": "Retroexcavadora FF Retro vista nocturna"},
    {"file": "14-tocon-extraccion.jpg", "alt": "Extracción de tocón con brazo JCB"},
    {"file": "15-zanja-drenaje.jpg", "alt": "Zanja de drenaje rural terminada"},
    {"file": "16-cano-saneamiento.jpg", "alt": "Caño de saneamiento colocado en zanja"},
]

GALLERY_VIDEOS: list[dict[str, str]] = [
    {"file": "01-trabajo.mp4", "poster": "01-barro-atardecer.jpg"},
    {"file": "02-trabajo.mp4", "poster": "06-trabajo-noche.jpg"},
    {"file": "03-trabajo.mp4", "poster": "10-nivelacion.jpg"},
]


def register_routes(app: Flask) -> None:
    @app.route("/")
    def index() -> str:
        return render_template(
            "index.html",
            services=SERVICES,
            gallery=GALLERY_IMAGES[:6],
        )

    @app.route("/servicios")
    def servicios() -> str:
        return render_template("servicios.html", services=SERVICES)

    @app.route("/galeria")
    def galeria() -> str:
        return render_template(
            "galeria.html",
            images=GALLERY_IMAGES,
            videos=GALLERY_VIDEOS,
        )

    @app.route("/contacto")
    def contacto() -> str:
        return render_template("contacto.html")

    @app.route("/robots.txt")
    def robots() -> Response:
        return send_from_directory(app.static_folder, "robots.txt")

    @app.route("/sitemap.xml")
    def sitemap() -> Response:
        return send_from_directory(app.static_folder, "sitemap.xml")
