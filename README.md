## $\textsf{\color{#A020F0}{trabalho-analise-processos}}$   
$\color{#32CD32}{\text{Grupo}}$ <br>
  Felipe Gabriel Kuhn<br>
  Thais Couto Henchen<br>

$\color{#32CD32}{\text{Contexto Ambiente}}$ <br>
  Distribuição Linux: Ubuntu Server/Desktop 26.04 LTS (Executado via VirtualBox).<br>
  Aplicação Analisada: Script Python multithread (app_diagnostico.py) simulando processamento contínuo de CPU e operações de entrada/saída (E/S).<br>

$\color{#32CD32}{\text{Análise Técnica dos Resultados}}$ <br>
  1-PID e PPID: Identificado o PID do processo filho e o PPID correspondente ao shell (bash), demonstrando a relação de criação e subordinação de processos.<br>
  2-Árvore de Processos: Verificada a hierarquia desde o processo de inicialização do sistema (systemd) até a execução do interpretador Python.<br>
  3-Estado e Recursos: Observado o processo nos estados S (Sleeping) e R (Running), registando o consumo pontual de CPU e memória RAM do sistema.<br>
  4-Threads: Confirmada a criação de Lightweight Processes (LWP/Threads) operando no mesmo espaço de endereçamento do processo pai.<br>
  5-Interface /proc/PID: Inspecionados os ficheiros /proc/PID/status, /proc/PID/limits, /proc/PID/cmdline e /proc/PID/fd, evidenciando como o Kernel Linux expõe métricas em tempo real.<br>
  $\color{#32CD32}{\text{6-Manipulação de Sinais:}}$ <br>
    SIGSTOP (19): Interrompeu a execução do processo mudando o estado para T (Stopped).<br>
    VSIGCONT (18): Retomou o estado de execução ativa.<br>
    SIGTERM (15): Encerrou o processo de forma graciosa e libertou os recursos alocados no sistema operacional.
