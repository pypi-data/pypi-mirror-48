# multiverseML

Aplicação para a criação de pipelines para desenvovimento de algoritmos de Machine Learning. A ideia é facilitar o acompanhamento das alterações de modelos, métricas e parâmetros sem preocupação com organização.

O <b>multiverseML</b> vem com a ideia de organizar o desenvolvimento no conceito de Multiverso. 

*O conceito de Multiverso tem suas raízes em extrapolações, até o momento não científicas, da moderna Cosmologia e na Teoria Quântica, e engloba também várias ideias oriundas da Teoria da Relatividade de modo a configurar um cenário em que pode ser possível a existência de inúmeros Universos onde, em escala global, todas as probabilidades e combinações ocorrem em algum dos universos. Simplesmente por haver espaço suficiente para acoplar outros universos numa estrutura dimensional maior: o chamado Multiverso.*
<https://pt.wikipedia.org/wiki/Multiverso_(ci%C3%AAncia)>

Dito isso, o <b>multiverseML</b> organizará o seu modelo nos conceitos de:

- <b>Multiverse(Multiverso):</b> Diretório central de armazenamento de todos os universos.
- <b>Universe(Universo):</b> O universo é todo arquivo no qual exista um monitoramento ativo. Um universo pode ser um desafio a ser resolvido, como uma identificação de fraude ou um reconhecimento de imagem.
- <b>Timeline(Linha do Tempo):</b> Cada Universo terá multiplas linhas temporais. Cada linha temporal será uma execução com sucesso do monitoramento. Cada linha temporal pode ter um modelo diferente, métricas diferentes e parâmetros diferentes. A timeline é baseada no versionamento do Git.
- <b>Reality(Realidade):</b> Realidade é a linha do tempo eleita para produção. Poder ser disponibilizado um servidor HTTP ou um processo Batch.


### Instalação versão 0.1.6-Alpha
`pip install multiverseML`

### Utilização

Para utilização é necessário primeiramente a importação do módulo:

`import multiverseml`

Após, será necessário definir qual será o nome do universo a ser criado. Seja criativo!

`universe = 'theoretical'`

Então criamos uma variável <i>model</i> com a finalidade de armazenar o nome e o modelo utilizado ("lr" no exemplo é um modelo de regressão linear).

```
    model = {
        'name': 'Linear Regression',
        'model': lr
    }
```

Agora vamos rastrear as métricas:

``` 
    metrics = {
        'rmse': rmse,
        'r2': r2,
        'mae': mae
    }
```

É possível também adicionar os parâmetros utilizados para o modelo.

```
    param = {
        'alpha': alpha,
        'l1_ratio': l1_ratio
    }
```

Por fim, deve-se enviar os dados para o <i>MultiverseML</i>.

`multiverseml.metrics(universe, model, metrics, param)`
    