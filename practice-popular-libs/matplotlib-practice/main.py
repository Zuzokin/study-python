import matplotlib.pyplot as plt
import numpy as np


# region Task 1
def visualize_temp_per_week():
    y = [25, 28, 30, 27, 22, 24, 26]
    x = np.arange(1, 8)

    plt.xlabel("День недели")
    plt.ylabel("Градусов цельсия")

    plt.xticks(ticks=x, labels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

    plt.plot(x, y)

    plt.show()


# endregion


# region Task 2
def visualize_interest():
    fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))
    # Creating dataset
    genres = ["Рок", "Поп", "Хип-Хоп", "Электронная", "Классическая"]

    data = [30, 20, 15, 10, 25]

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2.0 + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(
            genres[i],
            xy=(x, y),
            xytext=(1.35 * np.sign(x), 1.4 * y),
            horizontalalignment=horizontalalignment,
            **kw,
        )

    ax.set_title("Музыкальные предпочтения одногрупников", loc="right")
    plt.show()

    # # Creating plot
    # plt.pie(data, labels=genres)
    #
    # # show plot
    # plt.show()


# endregion


# region Task 3
def visualize_match_results():
    species = (
        "Матч 1",
        "Матч 2",
        "Матч 3",
        "Матч 4",
        "Матч 5",
    )
    weight_counts = {
        "Забито": np.array([2, 3, 1, 4, 2]),
        "Пропущено": np.array([1, 2, 0, 3, 1]),
    }
    width = 0.5

    fig, ax = plt.subplots()
    bottom = np.zeros(5)

    for boolean, weight_count in weight_counts.items():
        p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
        bottom += weight_count

    ax.bar_label(p, label_type="center")

    ax.set_title("Результаты матчей вашей любимой команды за последний сезон.")
    ax.legend(loc="upper right")

    plt.show()


# endregion


# region Task 4
def visualize_fruits_sales():
    # Example data
    fruits = ("Яблоки", "Груши", "Бананы", "Апельсины", "Персики")
    sales = np.array([100, 85, 70, 60, 45])

    fig, ax = plt.subplots(figsize=(10, 7))

    hbars = ax.barh(sales, width=sales, align="center")
    ax.set_yticks(sales, labels=fruits)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel("Продажи")
    ax.set_title("Продажи фруктов за последний месяц")

    plt.show()


# endregion


# region Task 5
def visualize_line():
    x = np.arange(0, 50)
    y = x * 3

    plt.legend()
    plt.grid()
    plt.plot(x, y)
    plt.show()


# endregion


# region Task 6
def visualize_graph():
    x = [10, 20, 30]
    y1 = [20, 40, 10]

    y2 = [40, 10, 30]

    plt.grid()
    plt.plot(x, y1, label="Синия линия")
    plt.plot(x, y2, label="Оранжевая линия")
    plt.legend()
    plt.show()


# endregion


# region Task 7
def visualize_visit_site_data():
    siteA = np.array([50, 60, 70, 80, 90])
    siteB = np.array([40, 55, 75, 85, 95])

    days = np.arange(1, 6)

    fig, axes = plt.subplots(1, 2)
    ax1 = axes[0]
    ax2 = axes[1]

    ax1.set(title="siteA")
    ax2.set(title="siteB")

    ax1.plot(days, siteA)
    ax2.plot(days, siteB)

    plt.show()


# endregion


# region Task 8
def visualize_popularity_of_programming_languages():
    fig, ax = plt.subplots()

    fruits = [
        "Javascript",
        "Java",
        "Python",
        "C#",
        "TypeScript",
        "PHP",
        "C++"
    ]
    percentage = [19.1, 14, 13.4, 13.3, 13.3, 7.1, 2.8]
    bar_colors = ["tab:red", "tab:blue", "tab:cyan", "tab:orange", "tab:green", "tab:purple", "tab:pink"]

    ax.bar(fruits, percentage, color=bar_colors)

    plt.minorticks_on()
    plt.grid(visible=True, which='major', color='r', linestyle=':', linewidth=0.5)
    plt.grid(visible=True, which='minor', linestyle=':', linewidth=0.5)

    ax.set_ylabel("Процентов проголосовавших")
    ax.set_title("Рейтинг языков программирования 2023")
    plt.show()


visualize_popularity_of_programming_languages()


# endregion


# region Task 9
def visualize_beautiful_stripes():
    fig, ax = plt.subplots()
    x = [i for i in range(10)]
    y = [i for i in range(3)]



# endregion


# region Task 10
def visualize_random_distribution():
    np.random.seed(42)
    x = np.random.uniform(-1, 1, 100)
    y = np.random.uniform(-1, 1, 100)
    plt.scatter(x, y)
    plt.show()

# visualize_random_distribution()
# endregion
