import os, re, json

# DIRETORIO DOS ARQUIVOS 
# dir = r'D:\\'
dir = r'C:\Users\Thiago xD\Downloads'

inserirNaPasta = False
removerDuplicados = False
visualizarDuplicados = True
salvarJson = False

# coloca o arquivo na pasta //  primeiro item e o nome da pasta, os seguintes são as extensoes
arquivoslist = {
    "favoritos": ['Favoritos','.acd','.bin','.abs','.eus','.docx'],
    "imagem": ['Imagens','.png','.jpg','.gif','.jpeg'],
    "arquivos": ['Arquivos','.exe','.msi'],
    "zipados": ['Compactados','.zip','.7z','.rar'],
    "PDF": ['Documentos pdf','.pdf'],
    "Videos": ['Videos','.mp4'],
    "Disc Image": ['Disck img','.iso'],
}

def pastCreator(list, arq):
    pathIn = os.path.join(dir,list[0])
    pathOld = os.path.join(dir,arq)    
    pathNew = os.path.join(dir,list[0],arq)      
    
    if not(os.path.exists(pathIn)):os.mkdir(pathIn)
    
    os.rename(pathOld, pathNew)
    
arquivos = os.listdir(dir)

#  ORGANIZAR EM PASTAS  ------
for list in arquivoslist.values():
    extensoes_list = list 
    
    for arquivo in arquivos :
        name, extensao = os.path.splitext(arquivo)
                
        if extensao.lower() in extensoes_list : 
            if inserirNaPasta == True:       
                pastCreator(extensoes_list, arquivo)                

# ---- ENCONTRA ARQUIVOS DUPLICADOS NA PASTA COMPLETA----

def RemoveDuplicate(root, arquivo):
    select = os.path.join(root,arquivo)
    os.remove(select)
    

number = 0
allArquiv = 0
duplicados = []

for roots, pastas, arquivos in os.walk(dir):
    
    for arquivo in arquivos:
        allArquiv+=1
        name, ext = os.path.splitext(arquivo)   
        #  limitado a encontrar 3 [ (999)] numeros, podendo colocar para encontrar 1 ou mais [ +?]      
        if(re.findall(r'.* \([0-9]{,3}\)$',name)) or re.findall(r'.*- Cópia',arquivo):                       
            number+=1           
            if visualizarDuplicados == True:
                print(arquivo)
                                
            if removerDuplicados == True:
                RemoveDuplicate(roots, arquivo) 
                
            if salvarJson == True:              
                                    
                duplicados.append({"arquivo":name, 
                                   'extensao': ext, 
                                   "caminho completo":os.path.join(roots,arquivo)}) 
                
                        
def organizeJson (index, arquivo):
    fileName = 'Duplicados'
    
    if not os.path.exists(f'{fileName}.json'): x = []
    else : x = json.load(open(f'{fileName}.json'))
            
    ar = {
        "id":index,
        "arquivo": arquivo['arquivo'],
        "extensao": arquivo['extensao'],
        "caminho completo": arquivo['caminho completo'],
    }
    
    x.append(ar)
    json.dump(x, open(f'{fileName}.json', 'w',encoding='UTF-8'),indent=4)    
      
if len(duplicados) != 0:        
    for index, x2 in enumerate(duplicados, start=1):
        organizeJson(index, x2)


print('Supostos Arquivos Duplicados => ',number)
print('Todos arquivos encontrados => ',allArquiv)


