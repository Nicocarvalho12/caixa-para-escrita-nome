from kivy.app import App # Importando a classe App
from kivy.uix.label import Label # Importando a classe Label
from kivy.uix.button import Button # Importando a classe Button
from kivy.uix.textinput import TextInput # Importando a classe TextInput
from kivy.uix.boxlayout import BoxLayout # Importando a classe BoxLayout
from kivy.uix.widget import Widget # Importando a classe Widget

#essa classe cria a janela do aplicativo
class BoasVindasApp(App): 
    def build(self):# Metodo build e chamado para construir a interface do usuário
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)


        # \\\\\\\\\\\\Titulo do aplicativo\\\\\\\\\\\\
        titulo = Label(    
            text='[b]App de Boas-vindas[/b]',
            font_size=34,
            size_hint=(1, 0.18),
            halign='center',
            valign='middle',
            markup=True,
            color=(0.2, 0.3, 0.7, 1)
        )
        titulo.bind(size=titulo.setter('text_size')) #essa linha esta vinculando o tamanho do texto ao tamanho do label, para que o texto seja centralizado corretamente.


        # \\\\\\\\\\\\Caixas de texto\\\\\\\\\\\\
        self.caixa_nome = TextInput( 
            hint_text='Digite seu nome',
            size_hint=(1, 0.13),
            font_size=20,
            multiline=False
        )

        # \\\\\\\\\\\\Caixa de texto para idade\\\\\\\\\\\\
        self.caixa_idade = TextInput( 
            hint_text='Digite sua idade',
            size_hint=(1, 0.13),
            font_size=20,
            input_filter='int',
            multiline=False
        )

        # \\\\\\\\\\\\Label para exibir mensagens\\\\\\\\\\\\
        self.label = Label( 
            text='',
            font_size=22,
            size_hint=(1, 0.22),
            halign='center',
            valign='middle',
            color=(0.1, 0.1, 0.1, 1)
        )
        self.label.bind(size=self.label.setter('text_size')) # essas linha esta vinculando o tamanho do texto ao tamanho do label, para que o texto seja centralizado corretamente.

        espaco = Widget() # Widget vazio para espaçamento

    
        # \\\\\\\\Botão para enviar as informações\\\\\\
        botao = Button( 
            text='Enviar',
            background_color=(0.2, 0.5, 0.8, 1),
            color=(1, 1, 1, 1),
            font_size=22,
            size_hint=(0.5, 0.12),
            pos_hint={'center_x': 0.5}
        )
        botao.bind(on_release=self.mostrar_mensagem) #essa linha esta vinculando o evento de clique do botão ao método mostrar_mensagem.

        layout.add_widget(titulo) #essa linha esta adicionando o titulo ao layout
        layout.add_widget(self.caixa_nome) #essa linha esta adicionando a caixa de texto para o nome ao layout  
        layout.add_widget(self.caixa_idade) #essa linha esta adicionando a caixa de texto para a idade ao layout
        layout.add_widget(self.label) #essa linha esta adicionando o label para exibir mensagens ao layout
        layout.add_widget(espaco) #essa linha esta adicionando o widget vazio para espaçamento ao layout
        layout.add_widget(botao) #essa linha esta adicionando o botão ao layout
        return layout

    def mostrar_mensagem(self, instance): # Metodo chamado quando o botão é pressionado
        #essa funcao esta recebendo o nome e a idade do usuario, validando as entradas e exibindo uma mensagem personalizada.
        nome = self.caixa_nome.text.strip() # Obtendo o nome do usuário
        idade_texto = self.caixa_idade.text.strip() # Obtendo a idade do usuário

        if not nome: # Verificando se o nome esta vazio
            self.label.text = '[color=ff0000]Por favor, digite seu nome.[/color]'
            self.label.markup = True
            return#se o nome do usuario estiver vazio, uma mensagem de erro aparecera.

        if not idade_texto:  # Verificando se a idade esta vazia
            self.label.text = '[color=ff0000]Por favor, digite sua idade.[/color]'
            self.label.markup = True 
            return #se a idade do usuario estiver vazia, uma mensagem de erro aparecera.

        try: 
            idade = int(idade_texto) # Convertendo a idade para um inteiro
        except ValueError: # Verificando se a conversão falhou
            self.label.text = '[color=ff0000]Sua idade esta invalida. Diga apenas numeros.[/color]' #se a conversão falhar, uma mensagem de erro aparecera.
            self.label.markup = True 
            return

        if idade >= 60:
            self.label.text = f'[color=008000]Olá, {nome}! Voce e idoso e mere muito respeito.[/color]' # se a idade  for igual ou maior que 60, uma mensagem alegando isso ira aparecer.
            self.label.markup = True
        elif idade >= 18:
            self.label.text = f'[color=0000ff]Olá, {nome}! Voce e maior de idade.[/color]' # se a idade for igual ou maior que 18, uma mensagem alegando isso ira aparecer.
            self.label.markup = True
        else:
            self.label.text = f'[color=ff9900]Olá, {nome}! Voce e menor de idade.[/color]' # se a idade for menor que 18, uma mensagem alegando isso ira aparecer.
            self.label.markup = True

if __name__ == '__main__': # Verifica se o script esta sendo executado diretamente
    BoasVindasApp().run()  # Cria uma instancia do aplicativo e executa o loop principal