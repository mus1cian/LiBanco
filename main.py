import streamlit as st
import cx_Oracle

st.title("LiBanco")
st.markdown("Aplicación de operaciones para sucursales y préstamos")

dsn = cx_Oracle.makedsn("172.17.0.2", "1521", "XE")
connection = cx_Oracle.connect("system", "admin", dsn=dsn)
cursor = connection.cursor()

opciones = ["Agregar", "Eliminar", "Actualizar"]

# Crea los botones de radio
eleccion = st.radio("Elige una opción", opciones)


def show_form1():
    if eleccion == "Agregar":
        idsucursal = st.text_input("Id Sucursal")
        nombresucursal = st.text_input("Nombre de Sucursal")
        ciudadsucursal = st.text_input("Ciudad Sucursal")
        activos = st.text_input("Activos")
        region = st.text_input("Región")
        if st.button("Finalizar"):
            #cursor.execute(f'EXEC INSERT_SUCURSAL({idsucursal}, {nombresucursal}, {ciudadsucursal}, {activos}, {region})')
            st.balloons();
    elif eleccion == "Eliminar":
        idsucursal = st.text_input("Id Sucursal")
        if st.button("Finalizar"):
            #cursor.execute(f'EXEC DELETE_SUCURSAL({idsucursal})')
            st.balloons();
    else:
        idsucursal = st.text_input("Id Sucursal")
        nombresucursal = st.text_input("Nombre de Sucursal")
        ciudadsucursal = st.text_input("Ciudad Sucursal")
        activos = st.text_input("Activos")
        region = st.text_input("Región")
        if st.button("Finalizar"):
            # cursor.execute(f'EXEC ACTUALIZAR_SUCURSAL({idsucursal}, {nombresucursal}, {ciudadsucursal}, {activos}, {region})')
            st.balloons();    
    

# Función que muestra el formulario 2
def show_form2():
    if eleccion == "Agregar":
    # Muestra la opción elegida
        idsucursal = st.text_input("Id Sucursal")
        noprestamo = st.text_input("Número de Préstamo")
        cantidad = st.text_input("Cantidad")
        if st.button("Finalizar"):
            # cursor.execute(f'EXEC INSERT_PRESTAMO({idsucursal}, {noprestamo}, {cantidad})')
            st.balloons();
    elif eleccion == "Eliminar":
        noprestamo = st.text_input("Id Sucursal")
        # cursor.execute(f'EXEC DELETE_PRESTAMO({noprestamo})')
        st.balloons();
    else:
        idsucursal = st.text_input("Id Sucursal")
        noprestamo = st.text_input("Número de Préstamo")
        cantidad = st.text_input("Cantidad")
        if st.button("Finalizar"):
            # cursor.execute(f'EXEC ACTUALIZAR_PRESTAMO({idsucursal}, {noprestamo}, {cantidad})')
            st.balloons();

def show_tables():
    # Execute a SQL query
    # cursor.execute("SELECT * FROM SUCURSAL")

    # Fetch results
    # results = cursor.fetchall()

    # Create a DataFrame from the results
    # df = pd.DataFrame(results, columns=[col[0] for col in cursor.description])

    # Display DataFrame as a table in Streamlit
    # st.write(df)

    # cursor.execute("SELECT * FROM PRESTAMOS ")

    # Fetch results
    # results = cursor.fetchall()

    # Create a DataFrame from the results
    # df = pd.DataFrame(results, columns=[col[0] for col in cursor.description])

    # Display DataFrame as a table in Streamlit
    # st.write(df)

    # Close cursor and connection
    # cursor.close()
    # connection.close()
    st.balloons(); 

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Sucursal"):
        show_form1()
with col2:
    if st.button("Préstamo"):
        show_form2()
with col3:
    if st.button("Ver tablas"):
        show_tables();
    

st.markdown("""
    <style>
    div.stButton button:first-child {
        background-color: #F63366 !important;
        color: #FFFFFF !important;
    }
    div.stButton button:hover {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-family: sans-serif;
    }
    div.stButton button:checked {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-family: sans-serif;
    }
    </style>
""", unsafe_allow_html=True)