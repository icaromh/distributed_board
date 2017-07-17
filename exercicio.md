# APS 4 – Aplicação Mural Distribuída

## Instruções Gerais
Nessa APS, a proposta é criar uma aplicação de um Mural Distribuído.

## Mural Distribuído
O Mural Distribuído é uma aplicação distribuída, onde vários usuários através de terminais
poderão postar mensagens em um monitor trazendo a ideia de um mural distribuído. Para isso, essa aplicação deve ser composta pelos seguintes módulos (poderão estar em máquinas
diferentes):

- Servidor: tem o papel de coordenar as mensagens do cliente para o monitor. Ou seja,
ele é o responsável por receber as mensagens dos terminais e encaminhar para o
mural quando solicitado.

- Terminal do cliente: a aplicação inicia solicitando o nome e a mensagem do usuário.
Depois, a aplicação envia os dados para o servidor e é finalizada. Vários terminais
podem executar em diferentes máquinas.

- Mural: esta aplicação irá solicitar ao servidor a próxima mensagem de tempos em
tempos (10 segundos). Se o servidor tiver uma mensagem, essa mensagem é
apresentada na tela junto com o nome do usuário (Fulano: Mensagem xxxxx). Se não
tiver, fica aguardando até a próxima solicitação.
Observação: neste desenvolvimento você pode utilizar RMI (Remote Method Invocation) ou
Web Services.



### Referências
-  http://docs.oracle.com/javase/7/docs/technotes/guides/rmi/hello/hello-world.html
-  http://www.devmedia.com.br/desenvolvendo-e-usando-web-services-em-java/37261

## Entrega
A entrega deve ser feita via Blackboard (no link dessa especificação) até o dia 30/06 às 22:00.


A atividade pode ser individual (ou em dupla) e caso ocorra cópia de trabalhos, todos os
envolvidos serão penalizados.
