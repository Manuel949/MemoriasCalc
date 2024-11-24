import streamlit as st
import pandas as pd
from docx import Document
from docx.shared import Inches
import matplotlib.pyplot as plt
import io



def main():
    st.title("GENERADOR DE MEMORIAS DE CÁLCULO")
    st.write("Introducir la información requerida para la generación de la memoria.")


    #Introduccion de plantilla
    template_file = st.file_uploader("Cargar plantilla de memoria", type="docx")

    if template_file:
        st.success("Plantilla cargada correctamente")
        #Introducción de datos
        st.subheader("Datos de la memoria")

        with st.form(key="form1"):
            proyecto=st.text_input("Nombre del proyecto")
            fecha=st.date_input("Fecha")
            autor=st.text_input("Autor")
            inicialesautor=st.text_input("Iniciales del autor")
            revisor=st.text_input("Revisor")
            inicialesrevisor=st.text_input("Iniciales del revisor")
            direccion=st.text_input("Dirección del proyecto")
            st.markdown("###### Coordenadas")
            latitud=st.text_input("Latitud")
            longitud=st.text_input("Longitud")

            st.markdown("##### Descripciones")
            descripcionarq=st.text_area("Descripción arquitectónica")
            st.markdown("###### Descripción de la estructura")
            descripciongrav=st.text_area("Descripción del sistema gravitacional")
            descripsistemlat=st.text_area("Descripción del sistema lateral")
            descripsistemcim=st.text_area("Descripción de la cimentación")

            st.markdown("##### Mecánica de suelos")
            autormecsuelos=st.text_input("Despacho que realizó estudio de mecánica de suelos")
            docmecsuelos=st.text_input("Nombre del informe de macánica de suelos")

            st.markdown("##### Información sísmica")
            #st.markdown("###### Tipo de norma")
            #boton_NTC=st.form_submit_button("NTC")
            #boton_CFE=st.form_submit_button("CFE")
            #boton_otranorma=st.form_submit_button("Otra norma")
            tipo_norma_sismo=st.selectbox("Tipo de norma", ["NTC","CFE", "Otra"])
            
            if tipo_norma_sismo=="CFE":
                normasismo=st.selectbox("Norma aplicable para análisis sísmico", ["CFE-MDOCS-2015", "CFE-MDOCS-2008"])
                st.write(f"La norma es: {normasismo}")
                regionsismoselect=st.selectbox("Región sismica",["A","B","C","D"])
                regionsismo=f"la región {regionsismoselect}"
                nivelzonificacion="la República Mexicana"
                st.write(f"tu regionsismo es: {regionsismo}")
                st.write(f"tu nivel de zonificacion es: {nivelzonificacion}")

            elif tipo_norma_sismo=="Otra":
                normasismo=st.text_input("Indicar norma")
                regionsismoselect=st.text_input("Región sismica")
                regionsismo=f"la región {regionsismoselect}"
                nivelzonificacion=st.text_input("Entidad (ciudad y/o pais)")
                st.write(f"la norma es: {normasismo}")
                st.write(f"tu regionsismo es: {regionsismo}")
                st.write(f"tu nivel de zonificacion es: {nivelzonificacion}")

            elif tipo_norma_sismo=="NTC":
                normasismo=st.selectbox("Norma aplicable para análisis sísmico", ["NTC-Sismo-2004", "NTC-Sismo-2017", "NTC-Sismo-2020", "NTC-Sismo-2023"])
                regionsismoselect=st.selectbox("Zona sismica",["I","II","III"])
                regionsismo=f"la zona {regionsismoselect}"
                nivelzonificacion="la Ciudad de México"
                st.write(f"la norma es: {normasismo}")
                st.write(f"tu regionsismo es: {regionsismo}")
                st.write(f"tu nivel de zonificacion es: {nivelzonificacion}")

            else:
                st.info("No se ha indicado norma aplicable")











         #   normasismo=st.selectbox("Norma aplicable para análisis sísmico", ["NTC-Sismo-2004", "NTC-Sismo-2017", "NTC-Sismo-2020", "NTC-Sismo-2023", "CFE-MDOCS-2015", "Otra"])
          #  st.write(f"La norma es: {normasismo}")

           # if normasismo=="CFE-MDOCS-2015":
           #     regionsismoselect=st.selectbox("Región sismica",["A","B","C","D"])
            #    regionsismo=f"la región {regionsismoselect}"
             #   nivelzonificacion="la República Mexicana"
              #  st.write(f"tu regionsismo es: {regionsismo}")
               # st.write(f"tu nivel de zonificacion es: {nivelzonificacion}")

         #   elif normasismo=="Otra":
          #      otra_norma=st.text_input("Indicar norma")
           #     regionsismoselect=st.text_input("Región sismica")
            #    regionsismo=f"la región {regionsismoselect}"
            #    nivelzonificacion=st.text_input("Entidad (ciudad y/o pais)")
            #    st.write(f"tu regionsismo es: {regionsismo}")
            #    st.write(f"tu nivel de zonificacion es: {nivelzonificacion}")
           # else:
           #     regionsismoselect=st.selectbox("Zona sismica",["I","II","III"])
            #    regionsismo=f"la zona {regionsismoselect}"
            #    nivelzonificacion="la Ciudad de México"
            #    st.write(f"tu regionsismo es: {regionsismo}")
            #    st.write(f"tu nivel de zonificacion es: {nivelzonificacion}") 
          
           


            



            submit_buttom=st.form_submit_button("Aplicar")
            if submit_buttom:
                st.write(proyecto)
                st.write(fecha)
                st.write(autor)
                st.write(inicialesautor)
                st.write(revisor)
                st.write(inicialesrevisor)
                st.write(direccion)
                st.write(latitud)
                st.write(longitud)
                st.write(descripcionarq)
                st.write(descripciongrav)
                st.write(descripsistemlat)
                st.write(descripsistemcim)
                st.write(autormecsuelos)
                st.write(docmecsuelos)
                st.write(normasismo)
                st.write(regionsismo)
                st.write(nivelzonificacion)
            else:
                st.info("Aun no se ejecuta")
                


    else: 
        st.warning("No se ha cargado plantilla")

main()














#def create_report(template_path, data, chart_data=None):
#    st.write("Iniciando la creación del informe...")
#    doc=Document(template_path)
#    for paragraph in doc.paragraphs:
#        for key, value in data.items():
#            if f'{{{{{key}}}}}' in paragraph.text:
#                st.write(f"Reemplazando {key} con {value} en el informe.")
#            paragraph.text=paragraph.text.replace(f'{{{{{key}}}}}', str(value))

#    if chart_data is not None:
#        st.write("Generando gráfico...")
#       plt.figure(figsize=(6,4))
#        plt.bar(chart_data['labels'],chart_data['values'])
#        plt.title(chart_data['title'])
#        plt.xlabel(chart_data.get('xlabel',''))
#        plt.ylabel(chart_data.get('ylabel',''))
#        img_buffer= io.BytesIO()
#        plt.savefig(img_buffer,format='png')
#        img_buffer.seek(0)
#        st.write("Insertando gráfico en el marcador del documento")
#        for paragraph in doc.paragraphs:
#            for run in paragraph.runs:
#                if '[Aquí se insertará el gráfico]' in run.text:
#                    run.text=run.text.replace('[Aquí se insertará el gráfico]', '')
#                    run.add_picture(img_buffer, width=Inches(6))


#    output=io.BytesIO()
#    doc.save(output)
#    output.seek(0)
#    st.write("Informe creado con éxito.")
#    return output


#def main():
#    st.title("Generador de informes desde plantillas")
#    template_file = st.file_uploader("Cargar plantilla Word", type="docx")
#    data_file = st.file_uploader("Cargar datos",type=["xlsx", "csv"])

#    if template_file and data_file:
#        st.success("Archivos cargados correctamente")
#        df = pd.read_csv(data_file) if data_file.name.endswith('.cvs') else pd.read_excel(data_file)
#        st.subheader("Datos cargados")
#        st.dataframe(df)

#        row_index=st.selectbox("Seleccionar fila para el informe", options=range(len(df)))
#        selected_data=df.iloc[row_index].to_dict()

#        generate_chart=st.checkbox("Generar gráfico")
#        chart_data=None

#        if generate_chart:
#            chart_title=st.text_input("Título del gráfico", "Gráfico de Datos")
#            x_column=st.selectbox("Columna para eje X", options=df.columns)
#            y_column=st.selectbox("Columna para eje Y", options=df.columns)

#            chart_data={
#                'title':chart_title,
#                'labels':df[x_column].tolist(),
#                'values':df[y_column].tolist(),
#                'xlabel':x_column
#            }

#            st.write("Datos del gráfico", chart_data)



#        if st.button("Generar Informe"):
#            output=create_report(template_file, selected_data,chart_data)
#            st.download_button("Descargar informe", output, "Informe_generado.docx", "application/vnd.openxmlformats-officedocument.wordprocessing.document")
               

#main()