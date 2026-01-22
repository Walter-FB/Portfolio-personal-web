from django.shortcuts import render, HttpResponse
from .models import ProductoJSON
from portfolio.models import Project

# Vista principal
def home(request):
    projects = Project.objects.all()
    return render(request, "core/home.html", {'projects': projects})

def about(request):
    productos = ProductoJSON.all()

    rutas = {
        'Arlistan_170g': 'core/img/Arlistan_170g.webp',
        'La_Virginia_170g': 'core/img/La_Virginia_170g.webp',
        'Dolca_170g': 'core/img/Dolca170g.webp',
        'Nescafe_Gold_100g': 'core/img/Nescafe_Gold_100g.webp',
        'DolceGusto_Espresso_10u': 'core/img/DolceGustoEspresso10u.webp',
        'La_Morenita_Brasil_10u': 'core/img/LaMorenitaBrasil10u.webp',
        'La_Virginia_Capuchino_125g': 'core/img/LaVirginiaCapuchino125g.webp',
        'Bonafide_Intenso_500g': 'core/img/BonafideIntenso500g.webp',
        'Dolca_Torrado_190g': 'core/img/Dolca_Torrado_190g.jpg',
        'yerba_Playadito_1kg': 'core/img/yerbaPlayadito1kg.webp',
        'yerba_Mananita_1kg': 'core/img/yerbaMananita1kg.webp',
        'yerba_Cruz_Malta_1kg': 'core/img/yerbaCruzMalta1kg.jpg',
        'yerba_La_Merced_500g': 'core/img/yerbaLaMerced500g.webp',
        'yerba_Taragui_500g': 'core/img/yerbaTaragui500g.webp',
        'yerba_Playadito_Premium_500g': 'core/img/yerbaPlayaditoPremium500g.webp',
        'yerba_Rosamonte_500g': 'core/img/yerbaRosamonte500g.jpg',
        'yerba_Nobleza_Gaucha_1kg': 'core/img/yerbaNoblezaGaucha1kg.jpg',
        'Té_Green_Hills_50_Saquitos': 'core/img/TéGreenHills50Saquitos.webp',
        'Té_Taragui_50_Saquitos': 'core/img/TéTaragui50Saquitos.webp',
        'Té_Green_Hills_Manzanilla': 'core/img/TéGreenHillsManzanilla.png'
    }

    nombres_presentables = {
        'Arlistan_170g': 'Arlistan 170g',
        'La_Virginia_170g': 'La Virginia 170g',
        'Dolca_170g': 'Dolca 170g',
        'Nescafe_Gold_100g': 'Nescafé Gold 100g',
        'DolceGusto_Espresso_10u': 'Dolce Gusto Espresso 10u',
        'La_Morenita_Brasil_10u': 'La Morenita Brasil 10u',
        'La_Virginia_Capuchino_125g': 'La Virginia Capuchino 125g',
        'Bonafide_Intenso_500g': 'Bonafide Intenso 500g',
        'Dolca_Torrado_190g': 'Dolca Torrado 190g',
        'yerba_Playadito_1kg': 'Yerba Playadito 1kg',
        'yerba_Mananita_1kg': 'Yerba Mañanita 1kg',
        'yerba_Cruz_Malta_1kg': 'Yerba Cruz de Malta 1kg',
        'yerba_La_Merced_500g': 'Yerba La Merced 500g',
        'yerba_Taragui_500g': 'Yerba Taragüí 500g',
        'yerba_Playadito_Premium_500g': 'Yerba Playadito Premium 500g',
        'yerba_Rosamonte_500g': 'Yerba Rosamonte 500g',
        'yerba_Nobleza_Gaucha_1kg': 'Yerba Nobleza Gaucha 1kg',
        'Té_Green_Hills_50_Saquitos': 'Té Green Hills 50 Saquitos',
        'Té_Taragui_50_Saquitos': 'Té Taragüí 50 Saquitos',
        'Té_Green_Hills_Manzanilla': 'Té Green Hills Manzanilla'
    }

    wins = {'Coto': 0, 'Día': 0, 'Jumbo': 0}

    for producto in productos:
        producto.imagen_url = rutas.get(producto.nombre, 'core/img/default-producto.jpg')
        producto.nombre_presentable = nombres_presentables.get(producto.nombre, producto.nombre.replace('_', ' '))

        # Precios formateados con puntos y sin decimales
        producto.precio_coto_f = "{:,.0f}".format(producto.precio_coto or 0).replace(",", ".")
        producto.precio_dia_f = "{:,.0f}".format(producto.precio_dia or 0).replace(",", ".")
        producto.precio_jumbo_f = "{:,.0f}".format(producto.precio_jumbo or 0).replace(",", ".")

        # Encontrar el precio más barato (ignorando None/0)
        precios = []
        if producto.precio_coto and producto.precio_coto > 0:
            precios.append(('coto', producto.precio_coto))
        if producto.precio_dia and producto.precio_dia > 0:
            precios.append(('dia', producto.precio_dia))
        if producto.precio_jumbo and producto.precio_jumbo > 0:
            precios.append(('jumbo', producto.precio_jumbo))
        
        # Marcar el más barato
        producto.is_cheapest_coto = False
        producto.is_cheapest_dia = False
        producto.is_cheapest_jumbo = False
        
        if precios:
            super_mas_barato = min(precios, key=lambda x: x[1])[0]
            if super_mas_barato == 'coto':
                producto.is_cheapest_coto = True
                wins['Coto'] += 1
            elif super_mas_barato == 'dia':
                producto.is_cheapest_dia = True
                wins['Día'] += 1
            elif super_mas_barato == 'jumbo':
                producto.is_cheapest_jumbo = True
                wins['Jumbo'] += 1

    # Invertir el orden de los productos
    productos.reverse()

    # Calcular ranking para el podio
    ranking = sorted(wins.items(), key=lambda x: x[1], reverse=True)
    podio = [
        {'puesto': 1, 'super': ranking[0][0], 'cantidad': ranking[0][1]},
        {'puesto': 2, 'super': ranking[1][0], 'cantidad': ranking[1][1]},
        {'puesto': 3, 'super': ranking[2][0], 'cantidad': ranking[2][1]}
    ]

    return render(request, "core/about.html", {'productos': productos, 'podio': podio})

# Vista de contacto
def contact(request):
    return render(request, "core/contact.html")

# Vista para testear la conexión al JSON
def test_conexion(request):
    try:
        productos = ProductoJSON.all()
        return HttpResponse(f"✅ Conexión exitosa. Hay {len(productos)} productos en el JSON.")
    except Exception as e:
        return HttpResponse(f"❌ Error al cargar datos: {e}")
