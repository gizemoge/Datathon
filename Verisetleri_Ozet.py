# NOTLAR

f_to_m_unpaid_care_work = pd.read_csv("datasets/1- female-to-male-ratio-of-time-devoted-to-unpaid-care-work.csv")
w_in_top_income_groups = pd.read_csv("datasets/2- share-of-women-in-top-income-groups.csv")
f_to_m_labor_force_part = pd.read_csv("datasets/3- ratio-of-female-to-male-labor-force-participation-rates-ilo-wdi.csv")
maternal_mortality = pd.read_csv("datasets/5- maternal-mortality.csv")
gender_wage_gap = pd.read_csv("datasets/6- gender-gap-in-average-wages-ilo.csv")
w_entrepreneurship = pd.read_csv("datasets/Labor Force-Women Entrpreneurship.csv", sep=";")
male_labor_force = pd.read_csv("datasets/Labour Force Participation - Male.csv")
female_labor_force = pd.read_csv("datasets/Labour Force Participation Female.csv")
placement = pd.read_csv("datasets/Placement.csv")
parliament = pd.read_excel("datasets/Parliament.xlsx")
adolescent_fertility_rate = pd.read_excel("datasets/Adolescent_Fertility_Rate.xlsx")
human_dev_indices = pd.read_excel("datasets/Human Development Composite Indices.xlsx")


1)  1- female-to-male-ratio-of-time-devoted-to-unpaid-care-work
    '''(Rapordan) Note: Gender inequality in unpaid care work refers to the female to
    male ratio of time spent in unpaid care work. The fitted value of the
    female share in the active population is estimated by controlling for
    the country’s GDP per capita, fertility rate, urbanisation rate, maternity
    leave policies and gender inequality in unemployment and education.'''

    f_to_m_unpaid_care_work.head()
    f_to_m_unpaid_care_work.shape
    #
    """
    Değişkenler:
        'Entity'
            Country
        'Code'
            Country code
        'Year'
            2014
        'Female to male ratio of time devoted to unpaid care work (OECD (2014))'
            Ne kadar çok kadın, erkeğe göre ev işi yükleniyor? 
            Min: 1.18
            Max: 17.29
    """

2)  2- share-of-women-in-top-income-groups
    w_in_top_income_groups.head()
    """
    Değişkenler:
        'Entity'
            Country
        'Code'
            Country code
        'Year'
        'Share of women in top 0.1%'
        'Share of women in top 0.25%'
        'Share of women in top 0.5%'
        'Share of women in top 1%'
        'Share of women in top 10%'
        'Share of women in top 5%'
    """

3)  3- ratio-of-female-to-male-labor-force-participation-rates-ilo-wdi
    f_to_m_labor_force_part.head()
    """
    Değişkenler:
        'Country'
        'Code'
        'Year'
        'Ratio of female to male labor force participation rate (%) (modeled ILO estimate)'
    """

#4 (1 ile aynı olduğu için silindi)

4)  5- maternal-mortality
    # The maternal mortality ratio is the number of women who die from pregnancy-related causes while pregnant or within 42 days of pregnancy termination per 100,000 live births.
    maternal_mortality.head()
    """
    Değişkenler:
        'Country'
        'Code'
        'Year'
        'Maternal Mortality Ratio (Gapminder (2010) and World Bank (2015))'
    """

5)  6- gender-gap-in-average-wages-ilo
    gender_wage_gap.head()
    """
    Değişkenler:
        'Entity'
            Country
        'Code'
            Country code
        'Year'
        'Gender wage gap (%)'
    """

6)  Labor Force-Women Entrpreneurship
    w_entrepreneurship.head()
    """
    Değişkenler:
        'No'
            Country code
        'Country'
        'Level of development'
            Developed 27, Developing 24
        'European Union Membership'
            Not member 31, Member 20
        'Currency'
            National Currency 36, Euro 15
        'Women Entrepreneurship Index'
        'Entrepreneurship Index'
        'Inflation rate'
        'Female Labor Force Participation Rate'
"""
    #Labour Force Participation - Male
    #Labour Force Participation Female

7)  Merged_labor_force
    """
    """

8)  Placement
    placement.head()
    """
    Değişkenler:
        'gender'
            M/F
        'ssc_percentage'
        'ssc_board'
            Others/Central
        'hsc_percentage'
        'hsc_board'
        'hsc_subject'
            Commerce 113
            Science 91
            Arts 11
        'degree_percentage'
        'undergrad_degree'
            Comm&Mgmt    145
            Sci&Tech      59
            Others        11
        'work_experience'
            No     141
            Yes     74
        'emp_test_percentage'
        'specialisation'
            Mkt&Fin    120
            Mkt&HR      95
        'mba_percent'
        'status'
            Placed/Not placed
    """
#Women Ent_Data3 (7 ile aynı olduğu için silindi)

9)  parliament

10) adolescent_fertility_rate

11) human_dev_indices


#########################

# Aşağıdaki verisetlerinde ülke isimlerini temsil eden Entity değişkeninin ismi, uyumluluk sağlamak için Country olarak değiştirildi.
    # f_to_m_unpaid_care_work
    # w_in_top_income_groups
    # gender_wage_gap

entity_dfs = [f_to_m_unpaid_care_work, w_in_top_income_groups, gender_wage_gap]

for df in entity_dfs:
    df.replace({"Entity":"Country"})

# Ülke kodlarını temsil eden Code değişkeni, veriseti birleştirme ve makine öğrenmesi süreçlerinde sorun yaratma olasılığına karşın drop edildi.
    # f_to_m_unpaid_care_work
    # w_in_top_income_groups
    # f_to_m_labor_force_part
    # maternal_mortality
    # gender_wage_gap
    # w_entrepreneurship (No)

code_drop_dfs = [f_to_m_unpaid_care_work, w_in_top_income_groups, f_to_m_labor_force_part, maternal_mortality, gender_wage_gap]

for df in code_drop_dfs:
    df.drop(columns="Code", inplace=True)

# Female labor force participation ve male labor force participation verisetleri birleştirildi
    # merged_labor_force

# Kadınların parlamento katılım oranları veriseti ve çocuk hamileliği veriseti eklendi.
    # Parliament
    # Adolescent_fertility_rate

