import random
import itertools
import json

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)


class Constants(BaseConstants):
    name_in_url = 'test_project'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):

    def creating_session(self):
        from .pages import initial_page_sequence
        ini = [i.__name__ for i in initial_page_sequence]
        for p in self.get_players():
            pb = ini.copy()
            random.shuffle(pb)
            p.page_sequence = json.dumps(pb)

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    page_sequence = models.StringField()

    m1500_1 = models.StringField(
        choices=['(1500 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 1',
        widget=widgets.RadioSelect)

    m1900_1 = models.StringField(
        choices=['(1900 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 1',
        widget=widgets.RadioSelect)

    m2300_1 = models.StringField(
        choices=['(2300 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 1',
        widget=widgets.RadioSelect)

    m2700_1 = models.StringField(
        choices=['(2700 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 1',
        widget=widgets.RadioSelect)

    m3100_1 = models.StringField(
        choices=['(3100 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 1',
        widget=widgets.RadioSelect)



    m1500_2 = models.StringField(
        choices=['(1500 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 2',
        widget=widgets.RadioSelect)

    m1900_2 = models.StringField(
        choices=['(1900 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 2',
        widget=widgets.RadioSelect)

    m2300_2 = models.StringField(
        choices=['(2300 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 2',
        widget=widgets.RadioSelect)

    m2700_2 = models.StringField(
        choices=['(2700 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 2',
        widget=widgets.RadioSelect)

    m3100_2 = models.StringField(
        choices=['(3100 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 2',
        widget=widgets.RadioSelect)



    m1500_5 = models.StringField(
        choices=['(1500 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 5',
        widget=widgets.RadioSelect)

    m1900_5 = models.StringField(
        choices=['(1900 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 5',
        widget=widgets.RadioSelect)

    m2300_5 = models.StringField(
        choices=['(2300 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 5',
        widget=widgets.RadioSelect)

    m2700_5 = models.StringField(
        choices=['(2700 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 5',
        widget=widgets.RadioSelect)

    m3100_5 = models.StringField(
        choices=['(3100 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 5',
        widget=widgets.RadioSelect)



    m1500_10 = models.StringField(
        choices=['(1500 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 10',
        widget=widgets.RadioSelect)

    m1900_10 = models.StringField(
        choices=['(1900 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 10',
        widget=widgets.RadioSelect)

    m2300_10 = models.StringField(
        choices=['(2300 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 10',
        widget=widgets.RadioSelect)

    m2700_10 = models.StringField(
        choices=['(2700 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 10',
        widget=widgets.RadioSelect)

    m3100_10 = models.StringField(
        choices=['(3100 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 10',
        widget=widgets.RadioSelect)



    m1500_20 = models.StringField(
        choices=['(1500 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 20',
        widget=widgets.RadioSelect)

    m1900_20 = models.StringField(
        choices=['(1900 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 20',
        widget=widgets.RadioSelect)

    m2300_20 = models.StringField(
        choices=['(2300 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 20',
        widget=widgets.RadioSelect)

    m2700_20 = models.StringField(
        choices=['(2700 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 20',
        widget=widgets.RadioSelect)

    m3100_20 = models.StringField(
        choices=['(3100 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 20',
        widget=widgets.RadioSelect)



    m1500_50 = models.StringField(
        choices=['(1500 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 50',
        widget=widgets.RadioSelect)

    m1900_50 = models.StringField(
        choices=['(1900 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 50',
        widget=widgets.RadioSelect)

    m2300_50 = models.StringField(
        choices=['(2300 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 50',
        widget=widgets.RadioSelect)

    m2700_50 = models.StringField(
        choices=['(2700 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 50',
        widget=widgets.RadioSelect)

    m3100_50 = models.StringField(
        choices=['(3100 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 50',
        widget=widgets.RadioSelect)



    m1500_100 = models.StringField(
        choices=['(1500 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 100',
        widget=widgets.RadioSelect)

    m1900_100 = models.StringField(
        choices=['(1900 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 100',
        widget=widgets.RadioSelect)

    m2300_100 = models.StringField(
        choices=['(2300 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 100',
        widget=widgets.RadioSelect)

    m2700_100 = models.StringField(
        choices=['(2700 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 100',
        widget=widgets.RadioSelect)

    m3100_100 = models.StringField(
        choices=['(3100 руб., 0 руб.)', '(1500 руб., 1500 руб.)'],
        label='Ваш выбор для дистанции 100',
        widget=widgets.RadioSelect)



    age = models.IntegerField(
        label='Возраст',
        min=13, max=125)

    gender = models.StringField(
        choices=['Женщина', 'Мужчина', 'Другое'],
        label='Пол',
        widget=widgets.RadioSelect)

    education = models.StringField(
        choices=('Среднее', 'Неоконченное высшее', 'Высшее'),
        label='Уровень образования',
        widget=widgets.RadioSelect)

    ed_type = models.StringField(
        choices=('Искусство и гуманитарные науки', 'Социальные науки, журналистика', 'Бизнес, управление и право',
                 'Естественные науки, математика и статистика', 'Информационные технологии', 'Инженерные и строительные науки',
                 'Сельскохозяйственные науки', 'Здравохранение и социальное обеспечение', 'Военные службы', 'Другое'),
        label='Область образования',
        widget=widgets.RadioSelect)

    h_population = models.StringField(
        choices=['менее 50 тыс. человек', '50 - 100 тыс. человек', '100 - 250 тыс.человек', '250 - 500 тыс. человек', '500 тыс. - 1 млн. человек', 'более 1 млн. человек'],
        label='Население в домашнем населенном пункте',
        widget=widgets.RadioSelect)

    civil_status = models.StringField(
        choices=['не замужен/не женат', 'замужем/женат', 'разведен(а)'],
        label='Семейное положение',
        widget=widgets.RadioSelect)

    religion = models.StringField(
        choices=['Буддизм', 'Христианство', 'Исслам', 'Атеизм', 'Другое'],
        label='Религия',
        widget=widgets.RadioSelect)

    etnos = models.StringField(
        choices=['Да', 'Нет'],
        label='Являетесь ли вы коренной этнической группой на территории проживания?',
        widget=widgets.RadioSelect)

    income = models.StringField(
        choices=['0 - 10 тыс. рублей', '10 - 25 тыс. рублей', '25 - 50 тыс. рублей', '50 - 100 тыс. рублей', 'более 100 тыс. рублей'],
        label='Среднемесячный доход',
        widget=widgets.RadioSelect)

    city = models.StringField(
        label='Город проживания')

    par_edu = models.StringField(
        choices=['Высшее у обоих', 'Высшее у одного родителя', 'Среднее', 'Другое'],
        label='Уровень образования родителей',
        widget=widgets.RadioSelect)

    work = models.StringField(
        choices=['Постоянная занятость', 'Временная занятость', 'Безработный'],
        label='Занятость',
        widget=widgets.RadioSelect)

    email = models.StringField(
        label='Электронная почта (так мы сможем добавить ваш выбор к предыдущим данным)')

    phone = models.StringField(
        label='Номер мобильного телефона')

    ch1 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='American Academy in Rome - совместный американо-итальянский университет искусств, предоставляющий гранты на обучение по всем основным видам искусства.',
        widget=widgets.RadioSelect)

    ch2 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Greenpeace - борьба с глобальными проблемами окружающей среды (не принимает пожертвований от государственных компаний, корпораций и политических партий).',
        widget=widgets.RadioSelect)

    ch3 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Asbestos Disease Awareness Organization - борьба с загрязнением асбестом и вызванными им заболеваниями (мезотелиома) в США.',
        widget=widgets.RadioSelect)

    ch4 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Salty Dog Paddle - уроки серфинга для собак, уроки по безопасности животных в воде, защита прав животных в США.',
        widget=widgets.RadioSelect)

    ch5 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label="Crohn's and Colitis Canada - борьба с болезнью Крона и язвенным колитом (разработка лекарств) в Канаде.",
        widget=widgets.RadioSelect)

    ch6 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label="American Association of Retired Persons - американский негосударственный инвестиционный фонд для помощи пенсионерам.",
        widget=widgets.RadioSelect)

    ch7 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label="Engineers Without Borders - международное научное сотрудничество с целью улучшения жизни развивающихся общин благодаря инженерным достижениям.",
        widget=widgets.RadioSelect)

    ch8 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label="World Wide Fund for Nature (WWF) - защита животных, сохранение видов, экологическое развитие по всему миру.",
        widget=widgets.RadioSelect)

    ch9 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label="Global Greengrants Fund - поддержка локальных движений за защиту природы по всему миру.",
        widget=widgets.RadioSelect)

    ch10 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label="International Medical Corps - медицинская помощь при гуманитарных катастрофах и повышение квалификации местных медицинских организаций по всему миру.",
        widget=widgets.RadioSelect)

    ch11 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label="Baan Gerda - забота о сиротах в Таиланде, с рождения больных ВИЧ.",
        widget=widgets.RadioSelect)

    ch12 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label="Eppley Foundation - поддержка физических и биологических исследованиий (включая борьбу с раком) в США.",
        widget=widgets.RadioSelect)

    ch13 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label="Movimento Sviluppo e Pace - программы постоянного трудоустройства для беднейших стран во всем мире.",
        widget=widgets.RadioSelect)

    ch14 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Алферовский фонд - поддержка российских научных проектов, стипендии молодым ученым и материальная помощь преподавателям высшей и средней школы.',
        widget=widgets.RadioSelect)

    ch15 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Благотворительный фонд "Центр охраны дикой природы" - охрана природы на территории бывшего СССР, защита заповедников и национальных парков.',
        widget=widgets.RadioSelect)

    ch16 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Royal Society for the Protection of Birds - сохранение исчезающих видов птиц на территории Великобритании.',
        widget=widgets.RadioSelect)

    ch17 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Благотворительный фонд защиты животных "БИМ" - сеть частных приютов (включая старейший в России) для бездомных животных.',
        widget=widgets.RadioSelect)

    ch18 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Best Friends Animal Society - питомники для животных в США.',
        widget=widgets.RadioSelect)

    ch19 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Mastercard Foundation - пожертвования в микрофинансовые программы для улучшения доступа людей по всему миру к глобальной экономике.',
        widget=widgets.RadioSelect)

    ch20 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Cancer Research UK - исследования с целью снижения смертности от рака и помощь больным раком в Великобритании.',
        widget=widgets.RadioSelect)

    ch21 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='The Canadian International Learning Foundation - профессиональное образование в регионах, затронутых войной, болезнями или бедностью (Афганистан, Йемен и Уганда).',
        widget=widgets.RadioSelect)

    ch22 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Wyoming Wildlife Federation - продвижение этических принципов в охоте и раболовстве, а также сохранение популяций животных в охотничьих зонах штата Вайоминг, США.',
        widget=widgets.RadioSelect)

    ch23 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Международный благотворительный фонд П.И.Чайковского - пропаганда российской музыкальной классики и обеспечение музыкальной литературой учебных заведений.',
        widget=widgets.RadioSelect)

    ch24 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Благотворительный фонд спасения тяжелобольных детей "Линия жизни" - снижение детской смертности от тяжелых заболеваний в России.',
        widget=widgets.RadioSelect)

    ch25 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Artforum Culture Foundation - греческая организация, занимающаяся современным искусством и культурным обменом.',
        widget=widgets.RadioSelect)

    ch26 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Aerospace Heritage Foundation of Canada - поддержка канадской космической отрасли.',
        widget=widgets.RadioSelect)

    ch27 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='International Literacy Foundation - борьба с неграмотностью во всем мире.',
        widget=widgets.RadioSelect)

    ch28 = models.StringField(
        choices=['1', '2', '5', '10', '20', '50', '100'],
        label='Calouste Gulbenkian Foundation - продвижение искусства, науки и образования в Португалии.',
        widget=widgets.RadioSelect)











