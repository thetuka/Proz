Instruções (PT/BR)
Faça um Fork deste repositório;
Clone localmente: git clone https://github.com/SEU_USERNAME/repositorio.git;
Adicione o remote upstream para manter seu repositório local atualizado. Por exemplo: git remote add upstream https://github.com/repositorio.git;
Utilize o comando git pull upstream main para baixar e mesclar as alterações no seu repositório local com base na branch main deste repositório original de onde você fez o fork, ou git fetch upstream main para baixar sem mesclar. Veja mais em: Primeiros Passos com Git e GitHub.

Crie/Referêncie uma nova branch e nomeie como feat/community/SEU_USERNAME:
Exemplo: git checkout -b feat/community/SEUNOME

Dentro da pasta community, crie um arquivo em Markdown (extensão .md) e nomeie com o mesmo nome do seu usuário no GitHub;
Exemplo: rafaeldscordeiro.md

Desenvolva o seu perfil. Para isso, você pode ver exemplos na pasta community e adicionar alguns dos utilitários presentes na pasta utils;
Observação: Use os outros exemplos como inspiração e não cópia.

Adicione suas alterações a "staging area" com o comando git add community/SEU_USERNAME.md;
Crie um commit e adicione a mensagem indicando a adição do seu perfil git commit -m"feat: add SEU_USERNAME profile";
Envie as alterações para o seu repositório remoto git push origin feat/community/SEU_USERNAME;
Crie um Pull Request.