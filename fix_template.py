
content = r"""{% extends 'core/base.html' %}

{% block title %}Coffe-City{% endblock %}

{% block background %}{% load static %}{% static 'core/img/bg.jpg' %}{% endblock %}

{% block headers %}
<h1>Caffeine Hub</h1>
<span class="subheading">Los mejores precios en un solo lugar</span>
{% endblock %}

{% block body_class %}cafe-fondo{% endblock %}

{% block content %}

<!-- Caffeine Hub Section -->
<div class="container" style="max-width: 900px; margin: 0 auto; padding: 0 20px;">
    <h1>Caffeine Hub - Scraper de Descuentos</h1>
    <br>
</div>
<p>
    <strong>Objetivo:</strong> Caffeine Hub busca visualizar todos los precios disponibles en el mercado, con los
    supermercados
    principales como representantes, con el objetivo de encontrar el precio más barato y poder comprobar de manera
    rápida si lo que estas pagando está bien o no. La temática son productos con cafeína, así que encontrarás
    exclusivamente de los mismos. <em>(Evitá los cafés torrados)</em>
    <br><br>
    ¿Por qué? Quería utilizar la programación para crear algo útil y se me ocurrió esto.
    Espero que te guste.
</p>

<br><br>

<div class="container">
    <div class="row">
        {% for cafe in productos %}
        <div class="col-md-6 mb-4">
            <div class="product-container">
                <div class="main-product text-center">
                    <img src="{% static cafe.imagen_url %}" alt="{{ cafe.nombre }}" class="product-img">
                    <h2 class="product-title">{{ cafe.nombre_presentable }}</h2>
                    <p class="product-description">Precios actuales:</p>
                </div>
                <div class="related-products d-flex justify-content-around align-items-center">
                    <div class="product-card">
                        <img src="{% static 'core/img/coto.png' %}" alt="Coto" class="supermarket-logo coto">
                        <p>Coto: {% if cafe.is_cheapest_coto %}<span style="color: #28a745; font-weight: bold;">🏆 ${{ cafe.precio_coto_f }}</span>{% else %}<strong>${{ cafe.precio_coto_f }}</strong>{% endif %}</p>
                    </div>
                    <div class="product-card">
                        <img src="{% static 'core/img/dia.png' %}" alt="Día" class="supermarket-logo dia">
                        <p>Día: {% if cafe.is_cheapest_dia %}<span style="color: #28a745; font-weight: bold;">🏆 ${{ cafe.precio_dia_f }}</span>{% else %}<strong>${{ cafe.precio_dia_f }}</strong>{% endif %}</p>
                    </div>
                    <div class="product-card">
                        <img src="{% static 'core/img/jumbo.webp' %}" alt="Jumbo" class="supermarket-logo jumbo">
                        <p>Jumbo: {% if cafe.is_cheapest_jumbo %}<span style="color: #28a745; font-weight: bold;">🏆 ${{ cafe.precio_jumbo_f }}</span>{% else %}<strong>${{ cafe.precio_jumbo_f }}</strong>{% endif %}</p>
                    </div>
                </div>
                <p class="fecha-Act">Actualizado: {{ cafe.fecha_actualizacion|date:"d/m/Y" }}</p>

            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
"""

with open(r'c:/Users/Walter/Desktop/django web personal/webpersonal-master/webpersonal/core/templates/core/about.html', 'w', encoding='utf-8') as f:
    f.write(content)
