<div style="text-align:center"><a href="https://www.youtube.com/watch?v=MlekK4aSm98"><img src="https://i.imgur.com/vCp9MPb.jpg" title="source: imgur.com" /></a></div>

<h3>Dlib – Treinamento de HOG com SVM para detecção de máscara no Ubuntu 18.04.5 usando ImgLab</h3>

<p>Baixar o repositório da biblioteca Dlib no GitHub<pp>

```
git clone https://github.com/davisking/dlib.git
```

<p>Navegar até dlib/tools/imglab e dar os comandos pelo terminal (conforme o arquivo README.txt)</p>

```
cd dlib/tools/imglab
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

<p>Após o processo, entrar na pasta build (dlib/tools/imglab/build)</p>

<p>Com o conjunto de imagens do dataset de treinamento em uma determinada pasta, executar o comando (incluir a barra após o último nome)</p>

```
./imglab -c nome_arquivo.xml /caminho_ate_dataset_treinamento/
```

<p>Exemplo

```
./imglab -c mask.xml /home/edee/Desktop/dlib_train/dataset/
```

<p>Então é criado o arquivo mask.xml que simplesmente lista as imagens da pasta especificada. O próximo passo é desenhar os retângulos que demarcam o objeto a ser detectado. O comando é:</p>

```
./imglab mask.xml
```

<p>Primeira coisa: Dar um nome para a label no campo ao lado direito de Next Label</p>
<p>Para desenhar o retângulo basta segurar a tecla Shift e marcar o ponto inicial e arrastar até o final.</p>

<p>Após acabar, salvar o arquivo (<b>File -> Save</b>). Com o comando ./imglab mask.xml verifica-se que os retângulos estão presentes em cada imagem.</p>

<p><b>[OPCIONAL]</b> Criar um arquivo xml com as imagens de validação

```
./imglab -c mask_validation.xml /home/edee/Desktop/dlib_train/dataset/validation/
```

```
./imglab mask_validation.xml
```

<p>Realizar o treinamento colando o arquivo de extensão <b>svm</b> na mesma pasta que o código. Testá-lo no conjunto de validação e posteriormente em imagens e vídeos diferentes.</p>

<b>Referências<b/>
<ul>
  <li>https://github.com/davisking/dlib/blob/master/python_examples/train_object_detector.py</li>
  <li>https://blog.codecentric.de/en/2018/10/diesel-car-hog-detector/</li>
  <li>https://handmap.github.io/dlib-classifier-for-object-detection/</li>
</ul>
