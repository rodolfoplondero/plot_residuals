import pandas as pd
import plotly.express as px
import re


def main():
    path = '.\\data\\'
    file_name = 'fl-2336'
    file_trn = path + file_name + ".trn"
    save_csv = False
    
    pattern_data = re.compile(
        "^(\s+(([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?\s+)+)(([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?(:([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?)+)\s+[0-9]+$")
    pattern_title = re.compile(
        "^(\s+([a-zA-Z]+\s+)+)[a-zA-Z]-[a-zA-Z]+\s+[a-zA-Z]-[a-zA-Z]+\s+[a-zA-Z]-[a-zA-Z]+\s+[a-zA-Z]+\s+k\s+[a-zA-Z]+\s+[a-zA-Z]+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?\s+p1\s+[a-zA-Z]+/[a-zA-Z]+$")

    columns = []
    lines = []

    for i, line in enumerate(open(file_trn)):
        if not columns:
            for match in re.finditer(pattern_title, line):
                columns = get_titles(match.group())

        for match in re.finditer(pattern_data, line):
            lines.append(match.group())

    lines = split_lines(lines.copy())

    # Create a DataFrame and convert data to float
    df = pd.DataFrame(data=lines, columns=columns)
    df.set_index("iter")

    del (df['time'])
    # for t in columns:
    #     if t != 'time':
    #         df[t] = df[t].astype(float)

    # Plot
    plot(df[-500:].copy())  # df[-500:] pega as 500 últimas iterações
    # plot(df[:500].copy())   # df[:500] pega as primeiras 500 iterações
    # plot(df[500:1000].copy())   # df[500:1000] pega entre 500 e 1000 iterações

    if save_csv:
        df.to_csv('.\\output\\residuos.csv', sep=';', index=False)

    print("Fim")


def get_titles(line: str):
    titles_list = line.replace("/", " ").strip().split(" ")
    titles_list[-1] = 'iteration'

    titles = []
    for title in titles_list:
        if title != "":
            titles.append(title)

    return titles.copy()


def split_lines(lines: list):
    for i in range(0, len(lines)):
        line_split = []
        for x in lines[i].strip().split(" "):
            if x != "":
                line_split.append(x)

        lines[i] = line_split

    return lines


def plot(df_plot: pd.DataFrame, save_file: bool = True, filename: str = "Teste.html"):
    remove_to_plot = ['iter', 'time', 'iteration']
    columns_to_plot = []

    for x in df_plot.columns:
        if x not in remove_to_plot:
            columns_to_plot.append(x)

    fig = px.line(df_plot, y=columns_to_plot, log_y=True)
    fig.update_layout(
        yaxis=dict(
            showexponent='all',
            exponentformat='power',
            title='Resíduos',
        ),
        xaxis=dict(
            exponentformat='none',
            title="Iterações"
        ),
        separators=',.'
    )

    if save_file:
        fig.write_html(f'.\\output\\{filename}')
    else:
        fig.show()


if __name__ == '__main__':
    main()
