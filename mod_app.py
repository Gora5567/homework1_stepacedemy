import streamlit as st
import random

tab1, tab2, tab3 = st.tabs(["первый урвоень", "второй уровень", "третий уровень"])
with tab1:
    st.header("первый уровень")

    random_number = random.randint(1, 4)

    option = st.selectbox("Выберите свое настроение в данный момент",
                        ["Веселый", "Уставший", "Программист", "Сонный"])
    answer = ""
    if random_number == 1:
        answer = "Не откладывай маленькие задачи — они быстро накапливаются."
    elif random_number == 2:
        answer = "Не бойся совершать ошибки — это часть обучения."
    elif random_number == 3:
        answer = "Не сравнивай свой прогресс с чужим — у каждого свой темп."
    elif random_number == 4:
        answer = "Делай перерывы во время учёбы, чтобы не перегружать мозг."

    if st.button("Получить совет"):
        st.success(answer)


    st.subheader('я немного не понял задание, так что сделаю два варианта, в первом кнопка выводит ответ рандомный а во втором ниже в зависимости от выбраного')
    option1 = st.selectbox("Выберите свое настроение в данный момент ",
                        ["Веселый ", "Уставший ", "Программист ", "Сонный "])
    answer = ""
    if option1 == "Веселый":
        answer = "Делись своей энергией с окружающими, но не забывай радовать и себя!"
    elif option1 == "Уставший":
        answer = "Не требуй от себя слишком многого. Сделай небольшую паузу и восстанови силы."
    elif option1 == "Программист":
        answer = "Не просто пиши код — старайся понимать, как он работает. Практика важнее зубрёжки!"
    else:
        answer = "Не жертвуй сном ради продуктивности. Хороший отдых поможет тебе завтра!"

    if st.button("Получить совет "):
        st.success(answer)
with tab2:
    conversion = st.sidebar.radio(
        "выберите тип конвертации:",
        ["километры в метры", "цельсий в фаренгейт"]
    )

    if conversion == "километры в метры":

        st.header("конвертер длины")

        meters = st.number_input("введите метры:", min_value=0.0)

        if st.button("конвертировать"):
            kilometers = meters / 1000
            st.metric(f"{kilometers} км")

    elif conversion == "цельсий в фаренгейт":

        st.header("конвертер температуры")

        celsius = st.number_input("введите температуру в градусах цельсий")

        if st.button("конвертировать"):
            fahrenheit = celsius * 1.8 + 32
            st.metric(f"{fahrenheit} °F")
with tab3:
    st.header("мини тест на знания пайтон")

    q1 = st.selectbox("вопрос первый, какой метод выводит значение в консоль",
                    ["def", "print", "concat", "upper"])

    q2 = st.selectbox("вопрос второй, с помощью какой команды создается функция",
                    ["def", "print", "concat", "upper"])

    q3 = st.selectbox("вопрос третий, какой метод изменяет строку только на большие буквы",
                    ["def", "print", "concat", "upper"])

    progress_placeholder = st.empty()

    if st.button("подтвердить результаты"):
        score = 0

        if q1 == "print":
            score += 1

        if q2 == "def":
            score += 1

        if q3 == "upper":
            score += 1

        progress_placeholder.progress(score / 3)

        st.metric("Твой результат", f"{score} / 3")

        if score == 3:
            st.success("все гуд")
            st.balloons()

        elif score == 2:
            st.info("норм")

        elif score == 1:
            st.warning("плохо")

        else:
            st.error("перепройди тест")