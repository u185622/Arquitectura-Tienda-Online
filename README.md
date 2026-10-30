# Tienda Online

Hecho por **Unai Lama Pérez** para la asignatura de Arquitectura del Software.

## ¿De qué va esto?

Es una tienda online hecha en Python, sin interfaz gráfica, que funciona por consola.

La idea es sencilla: en la tienda hay usuarios, productos y pedidos. Los usuarios pueden ser
clientes o administradores, y solo los clientes pueden hacer pedidos. Cuando un cliente compra algo,
el programa mira si queda stock suficiente; si lo hay, crea el pedido, calcula el total y resta las
unidades del inventario.

Hay tres tipos de productos: los normales, los electrónicos (que tienen meses de garantía) y la ropa
(que tiene talla y color). También se puede ver el historial de pedidos de cada cliente, ordenado
por fecha.

## Cómo está organizado

El código está repartido en carpetas para que no esté todo en un solo archivo:

- `models/` tiene las clases básicas: los productos, los usuarios y los pedidos.
- `services/` tiene `TiendaService`, que es la que se encarga de todo: registrar usuarios, añadir
  productos, hacer pedidos, etc.
- `main.py` es una prueba que crea unos cuantos usuarios y productos, hace tres pedidos y enseña
  por pantalla cómo queda todo.

## Cómo ejecutarlo

Solo necesitas tener Python instalado, no hace falta instalar ninguna librería:

```bash
cd Tienda_online
python main.py
```

Verás el inventario del principio, los pedidos que se han hecho, el historial de un cliente y cómo
ha bajado el stock al final.

## Ramas

En `main` está la versión que funciona. Cada cosa nueva la hago en su propia rama
(`feature/algo`, por ejemplo `feature/docker`) y cuando está terminada la junto con `main` mediante
un Pull Request.
