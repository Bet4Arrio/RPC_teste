
import pandas as pd



COLUMNS = ["name", "house", "Dívida", "Capacidade de pagamento anual"]
TO_NUM_COLUMNS = [ "Dívida", "Capacidade de pagamento anual"]
TARGET_COLUMN = 'Dívida'
# TARGET_COLUMN = 'Capacidade de pagamento anual'

def get_abc_class(percentage):
    
    if percentage <= 50:
        return 'A'
    elif percentage <= 80:
        return 'B'
    else:
        return 'C'


def get_alive_df()->pd.DataFrame:
    corretistas = pd.read_csv("original_db/correntistas_banco_bravos_1.csv",    
                                            sep=";",encoding="ISO-8859-1")
    obitos = pd.read_csv("original_db/correntistas_obito_1.csv", sep=";")
    #Limpando Dados
    df = corretistas[~corretistas.name.isin(obitos.Name)]
    df = df[df[TARGET_COLUMN].notna()]
    #Salvando
    df.to_csv("vivos.csv", index=False)
    return df

def get_correct_df(df:pd.DataFrame, columns:list)->pd.DataFrame:
    #Tirar caracters textuas dos numeros, e muda , por . 
    
    rm_text_el = lambda x: x.replace('R$','').replace(".", "").replace(",", '.')
    
    # Transformando o dinheiro em Numeros 
    for col in TO_NUM_COLUMNS:
        df.loc[df[col].notna(), col] = pd.to_numeric(
                                                       df.loc[df[col]
                                                       .notna(), col]
                                                       .apply(rm_text_el))
    
    return df[columns]

def get_abc_classes(df:pd.DataFrame, col_names) -> pd.DataFrame:
    for col_name in col_names:
        # Ordenando
        df = df.sort_values(col_name, ascending=False)

        # Calculando porcetual de influencia de cada pessoa
        df[col_name+'_sum'] = df[col_name].cumsum()
        df.loc[:,col_name+'_porcentagem'] = (df[col_name+'_sum'] / 
                                                df[col_name].sum()) * 100
        
        df[col_name+'_abc_class'] = df[col_name+'_porcentagem'].apply(get_abc_class)
    return df



def main() -> None:
    # Lendo arquivos
    df = get_correct_df(get_alive_df(), COLUMNS)
    # name
    
    person = get_abc_classes(df, TO_NUM_COLUMNS)
    houses = get_abc_classes(df.groupby("house").sum(), TO_NUM_COLUMNS)

    person.to_csv("abc_person_all.csv", index=False)
    houses.to_csv("abc_houses_alll.csv")


if __name__ == "__main__":
    main()