Para que possamos rodar o back-end, é preciso que siga as seguintes instruções:

É necessário ter o python com pip instalado

no terminal

1 - Prceisamos instalar as dependências do projeto, para isto, utilizamos o seguinte comando: "pip install <nome>"
  
2 - É necessário instalar também o uvicorn, que é o nosso servidor. Para isto, utilizamos o seguinte comando: "pip install uvicorn"
  
3 - Enfim, vamos dá início em nossa aplicação utilizando o seguinte comando: "uvicorn << aquivo principal >>:<< variavel que recebe o FasAPI >> --reload" 

OBS: o "--reload" é responsável por detectar qualquer mudança em nosso projeto e rebuildar logo em seguida. Sendo assim, não será necessário para 
a aplicação para realizar novas implementações
  
Então, nosso comando para execução do projeto será: "uvicorn main:app --reload"
  
 O projeto esta configurado para rodar local na porta 8000.


para rodarmos a aplicação basta seguir os passos abaixo: 

1 - docker build -t nomeAplicacao . (docker build -t sprint3_back .) 

2 - docker run -p portaExposta:portaContainer nomeAplicacao (docker run -p 5001:8000 sprint3_back
