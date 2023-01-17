import pandas as pd
import streamlit as st
import time

st.title('Streamlit demo')

dataset_file = st.file_uploader('Choose your dataset')

if dataset_file:
    dataset = pd.read_csv(dataset_file)

    st.write(dataset)

    columns = list(dataset.columns)


    selected_column = st.selectbox('select a column', columns)

    if st.button('plot'):
        progress_status = st.sidebar.empty()
        progress = st.sidebar.progress(0)

        data = list(dataset[selected_column])

        rows = [data[0]]

        chart = st.line_chart(rows)

        for i in range(1, len(data)):
            y = data[i]

            chart.add_rows([y])

            percentage = i / len(data)
            progress.progress(percentage)
            progress_status.text('{:.2f}%'.format(percentage))

            time.sleep(.05)

        progress.empty()
        progress_status.text('done!')

        st.success('plotted')


