# Bot de Arbitragem de Criptomoedas

## Descrição
O **Bot de Arbitragem de Criptomoedas** é um sistema privado e exclusivo, desenvolvido para identificar e executar operações de arbitragem entre diferentes corretoras de criptomoedas, permitindo ao usuário explorar diferenças de preços para obter lucro.

O projeto inclui:
- **Execução Automática** de ordens de compra e venda.
- **Monitoramento em Tempo Real** de preços.
- **Interface Gráfica com PyQt6** para facilitar a interação do usuário.
- **Sistema de Autenticação e Ativação** com código de acesso.
- **Logs e Alertas** para acompanhamento de operações.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Bibliotecas:**
  - `ccxt` para interação com corretoras
  - `PyQt6` para interface gráfica
  - `requests` para chamadas API
  - `sqlite3` para armazenamento local de configurações
- **Corretoras Suportadas:** Binance, KuCoin (mais serão adicionadas futuramente)

## Funcionalidades
- **Adicionação de API Keys**: Usuário pode inserir as chaves da Binance e KuCoin pela interface.
- **Esconder API Keys**: Campos de entrada das chaves desaparecem após a configuração.
- **Monitoramento de Preços**: Atualização em tempo real dos preços das criptomoedas.
- **Execução de Ordens**: Compra e venda automática de criptoativos quando uma oportunidade de arbitragem é detectada.
- **Sistema de Ativação**: Requer um código de autorização para funcionar.
- **Persistência de Ativação**: O bot lembra a ativação para que não precise digitar o código toda vez.
- **Logs de Operações**: Registros detalhados das negociações realizadas.
- **Alertas e Notificações**: Opção futura para enviar alertas via Telegram, WhatsApp ou pop-ups.

## Instalação
Este projeto é particular e não está disponível para distribuição pública. Caso tenha permissão de uso, siga as instruções internas para instalação e configuração.

## Configuração
Antes de rodar o bot, configure suas chaves de API diretamente pela interface do aplicativo. O acesso ao sistema requer ativação por meio de um código exclusivo.

## Uso
1. **Inicie o bot** e insira suas credenciais.
2. **Acompanhe os preços e oportunidades** pela interface.
3. **Ajuste parâmetros** como volume e limite de risco.
4. **Deixe o bot rodando** e monitorando as operações.

## Segurança
- Nunca compartilhe suas API Keys.
- Habilite **somente permissões de leitura e trading** na API das corretoras.
- O bot **não solicita permissão de saque**, garantindo mais segurança.
- O código de ativação é único e intransferível.

## Futuras Melhorias
- Suporte a mais corretoras.
- Integração com WebSocket para respostas mais rápidas.
- Implementação de módulo de Machine Learning para otimizar operações.

## Direitos Autorais
Este projeto é **privado** e **não pode ser redistribuído ou compartilhado** sem autorização.

## Contato
Caso tenha dúvidas ou sugestões, entre em contato pelo e-mail: **jmfelicio.sp@gmail.com**.

