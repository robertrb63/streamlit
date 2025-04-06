
# pip install pandas

import streamlit as st   # pip install streamlit
import random
import requests

# Asi se crea el randerizado  y pagina web
st.set_page_config(
    page_title="Pokémon Generator", 
    page_icon=":tada:", 
    layout="centered")
# Definimos la función que genera datos aleatorios
def get_pokemon_data(pokemon_name):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Pokémon no encontrado.")
            return None
    except:
        st.error("Error al obtener los datos del Pokémon.")
        return None
    
def get_random_pokemon():
    pokemon_id = random.randint(1, 898)  # Hay 898 Pokémon en total
    return get_pokemon_data(str(pokemon_id))


st.title("Pokémon Generator")
st.markdown("Generador de Pokémon aleatorio usando la API de PokéAPI.")

col1, col2 = st.columns([2, 1])
with col1:
    pokemon_name = st.text_input("Ingresa el nombre del Pokémon:")
with col2:
    random_button = st.button("Generar Pokémon Aleatorio")

pokemon_data = None
if pokemon_name:
    pokemon_data = get_pokemon_data(pokemon_name)
elif random_button:
    pokemon_data = get_random_pokemon()

if pokemon_data:
    img_col, info_col = st.columns([3, 1])

    with img_col:
        st.image(
            pokemon_data["sprites"]["other"]["official-artwork"]["front_default"], 
            caption=f"#{pokemon_data['id']}  {pokemon_data['name'].title()}",
            use_container_width=True
        )
    with info_col:
            st.subheader("Información del Pokémon")
            st.write(f"Nombre: {pokemon_data['name'].title()}"),
            st.write(f"Altura: {pokemon_data['height']/10} m"),
            st.write(f"Peso: {pokemon_data['weight']/10} kg"),

            st.subheader("Tipos")
            tipos = [tipo["type"]["name"].title() for tipo in pokemon_data["types"]]
            for tipo in tipos:
                st.write(f"- {tipo.title()}")

    
#  print(get_pokemon_data("pikachu"))  # Ejemplo de uso de la función

