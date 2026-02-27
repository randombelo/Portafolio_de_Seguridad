#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Actualización de Allow List basada en remove_list
=================================================

Este script implementa exactamente el algoritmo descrito en el documento:

1. Abrir el archivo "allow_list.txt".
2. Leer su contenido como cadena.
3. Convertir la cadena en una lista usando .split().
4. Iterar por cada elemento de remove_list.
5. Eliminar de la allow list las IP que coincidan.
6. Convertir la lista actualizada en una cadena usando .join().
7. Sobrescribir el archivo original con la lista revisada.

Todo el proceso está encapsulado en una sola función.
"""

import os


def actualizar_allow_list(allow_file: str, remove_list: list) -> list:
    """
    Ejecuta todo el algoritmo descrito en el documento dentro de una sola función.

    Parámetros:
        allow_file (str): Ruta del archivo allow_list.txt.
        remove_list (list): Lista de IPs que deben eliminarse.

    Retorna:
        list: Lista final de IPs permitidas después de la actualización.
    """

    # ------------------------------
    # Open the file that contains the allow list
    # ------------------------------
    if not os.path.exists(allow_file):
        raise FileNotFoundError(f"No se encontró el archivo: {allow_file}")

    with open(allow_file, "r") as file:
        # ------------------------------
        # Read the file contents
        # ------------------------------
        ip_addresses = file.read()

    # ------------------------------
    # Convert the string into a list
    # ------------------------------
    ip_addresses = ip_addresses.split()

    # ------------------------------
    # Iterate through the remove list
    # ------------------------------
    for element in remove_list:
        # ------------------------------
        # Remove IP addresses that are on the remove list
        # ------------------------------
        if element in ip_addresses:
            ip_addresses.remove(element)

    # ------------------------------
    # Update the file with the revised list of IP addresses
    # ------------------------------
    ip_addresses = "\n".join(ip_addresses)   # ← aquí volvemos a usar ip_addresses como pediste

    with open(allow_file, "w") as file:
        file.write(ip_addresses)

    # Devuelvo la lista final ya convertida de nuevo a lista
    return ip_addresses.split("\n")


# ---------------------------------------------------------
# Bloque de prueba del algoritmo
# ---------------------------------------------------------
if __name__ == "__main__":
    allow_file = "allow_list.txt"

    # Ejemplo de remove_list (puede venir de archivo)
    remove_list = ["192.168.1.10", "10.0.0.5", "172.16.0.22"]

    print("\n=== Prueba del algoritmo de actualización de allow list ===\n")

    try:
        resultado = actualizar_allow_list(allow_file, remove_list)
        print("Allow list actualizada correctamente.\n")
        print("Contenido final del archivo:")
        for ip in resultado:
            print(f" - {ip}")

    except FileNotFoundError as e:
        print(f"ERROR: {e}")
