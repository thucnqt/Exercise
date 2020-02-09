# Game Black Jack !
# Khai báo thư viện:
# Dùng thư viện random vì để xáo trộn bộ bài trước khi chia 
import random

# Khai báo các biến toàn cục
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# Khai báo một biến Boolean để kiểm soát vòng lặp While 
playing = True
# Khởi tạo Class

# Tạo class Card: Xây dựng lá bài gồm 2 thuộc tính là: suit và rank (chất và bậc)

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    # Hàm này khi được hỏi lá bài sẽ trả về  một chuỗi theo format: Rank + of + suit
    def __str__(self):
        return self.rank + ' of ' + self.suit

# Tạo class Deck: với ý tưởng lưu trữ 52 đối tượng thẻ trong một danh sách (list) mà sau đó có thể sáo trộn (shuffle)

class Deck:
    def __init__(self):
        self.deck = [] # Khai bao mot list de luu tru
        # Dùng vòng lặp để xây dựng 52 thẻ của 1 bộ bài, sau đó chúng ta thêm nó vào list đã khởi tạo.
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    # Xây dựng hàm __str__ để ứng với mỗi đối tượng, in ra mội chuỗi string 
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp
    # Hàm xáo bài khi đã lưu trữ 52 lá           
    def shuffle(self):
        random.shuffle(self.deck)
    # Hàm lấy bài trong 52 lá 
    def deal(self):
        single_card = self.deck.pop()
        return single_card

# Tạo Class Hand dùng để tính giá trị các quân bài, và tùy chỉnh giá trị quân Ace cho phù hợp

class Hand:
    def __init__ (self):
        self.cards = [] 
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card) # Thêm lá bài vào một mảng mới khởi tạo 
        self.value += values[card.rank] # lấy giá trị ứng với rank của quân bài
        # Kiểm tra lá bài có phải quân Ace không? Nếu phải tăng biến đếm lên 1
        if card.rank == 'Ace':
            self.aces +=1
        # Hàm tùy chỉnh tính điểm khi có quân Ace
    def adjust_for_ace(self):
        # Vòng lập: Nếu tổng điểm lớn hơn 21 và tồn tại quân Ace thì sẽ chạy. 
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.name = ''
        self.total = 0 # This can be set to a default value or supplied by a user input
        self.bet = 0
    # Khởi tạo các hàm tính nếu win được cộng tiền nếu thua bị trừ tiền đặt cược
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -+ self.bet

#Taking bets#



# taking hits#
# Class xử lí quá trình chơi (Rút tiếp bài hoặc dừng)
class Process:
    def __init__(self):
        pass

    def take_bet(self,chips):
        chips.name = str(input('May ten gi: '))
        chips.total = int(input('So tien quy ra chip la: '))

        while True:
            try:
                chips.bet = int(input('Số chip bạn muốn đặt cược  '))
            except ValueError:
                print("Xin lỗi, vui lòng nhập số tiền bằng số tự nhiên")
            else:
                if chips.bet > chips.total:
                    print('Xin lỗi, số tiền của bạn khôn thể cao hơn trong tài khoản {} '.format(chips.total))
                else:
                    break      

    def hit(self,deck,hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    # Hàm hỏi lấy hay dừng rút quân bài
    def hit_or_stand(self,deck,hand):
        global playing
        
        while True:
            x = input("Bạn có muốn lấy (h) hay dừng (s)? Nếu lấy ấn phím h và dừng ấn phím s:  ")
            
            if x[0].lower() == 'h':
                self.hit(deck,hand)  # hit() function defined above

            elif x[0].lower() == 's':
                print("Người chơi dừng lấy, nhà cái đang rút bài")
                playing = False

            else:
                print("Vui lòng nhập đụng kí tự ạ ! Xin cám ơn (h: lấy ; s: dừng)")
                continue
            break

    # Hàm hiển thị tông tin người chơi và nhà cái
class Show:
    def __init__(self):
            pass

    def show_some(self,player,dealer):
        print("\nDealer's Hand")
        print("<card hidden>")
        print(' ', dealer.cards[1])
        print("\nPlayer's Hand: ", *player.cards, sep= '\n')
        # print("\nTotal value: ", )
                
    def show_all(self,player,dealer):
        print("\nDealer's Hand:", *dealer.cards, sep="\n")
        print("Dealer's Hand =",dealer.value)
        print("\nPlayer's Hand: ", *player.cards, sep= '\n')
        print("Player's Hand = ", player.value)

    #Hàm khi người chơi bị bust ( trên 21 điểm) và bị trừ chip
    def player_busts(self,player,dealer,chips):
        print("Player busts!")
        chips.lose_bet()
    # Người chơi win và được thêm chip
    def player_wins(self,player,dealer,chips):
        print("Player wins!")
        chips.win_bet()
    # Nhà cái bust > 21 điểm và người chơi được + chip
    def dealer_busts(self,player,dealer,chips):
        print("Dealer busts!")
        chips.win_bet()
    # Nhà cái win và người chơi mất chip
    def dealer_wins(self,player,dealer,chips):
        print("Dealer wins!")
        chips.lose_bet()
        # Push Khi cả 2 cùng bằng điểm 
    def push(self,player,dealer):
        print("Dealer and Player tie! It's a push.")    

#NOW FOR THE GAME

class Game:
    def __init__(self):
        pass

    def play(self):
        global playing
        while True:
            # Print an opening statement
            print("Chào mừng đến với sòng bạc CTC !!")
            
            # Create & shuffle the deck, deal two cards to each player
            deck = Deck()
            deck.shuffle()
            
            player_hand = Hand()
            player_hand.add_card(deck.deal())
            player_hand.add_card(deck.deal())
            
            dealer_hand = Hand()
            dealer_hand.add_card(deck.deal())
            dealer_hand.add_card(deck.deal())
            
            # Set up the Player's chips
            player_chips = Chips()
            a  = Show()
            b = Process()
            # Prompt the Player for their bet
            b.take_bet(player_chips)
            
            # Show cards (but keep one dealer card hidden)
            a.show_some(player_hand, dealer_hand)
            
            while playing:  
                
                # Prompt for Player to Hit or Stand
                b.hit_or_stand(deck, player_hand)
                
                # Show cards (but keep one dealer card hidden)
                a.show_some(player_hand,dealer_hand) 
                
                # If player's hand exceeds 21, run player_busts() and break out of loop
                if player_hand.value >21:
                    a.player_busts(player_hand, dealer_hand, player_chips)

                    break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            # Khi người chơi tổng điểm dưới 21
            if player_hand.value <= 21:
                # Nếu nhà cái dưới 17 điểm tì rút tiếp, > 17 thì dừng và hiển thị thông tin cả 2 
                while dealer_hand.value <17:
                    b.hit(deck, dealer_hand)
            
                # Show all cards
                a.show_all(player_hand,dealer_hand)
                
                # Run different winning scenarios
                # Tính điểm xem ai là người chiến thắng, người chơi chiến thắng được chip, thua bị trừ chip, hòa thì bình thường
                if dealer_hand.value > 21:
                    a.dealer_busts(player_hand,dealer_hand,player_chips)

                elif dealer_hand.value > player_hand.value:
                    a.dealer_wins(player_hand,dealer_hand,player_chips)

                elif dealer_hand.value < player_hand.value:
                    a.player_wins(player_hand,dealer_hand,player_chips)

                else:
                    a.push(player_hand,dealer_hand)
                
            
            # Inform Player of their chips total
            print("\nNgài / Quý cô {} Sau tất cả mình còn là: {} ".format(player_chips.name,player_chips.total))
            
            # Ask to play again
            # Khởi tạo 1 game mới :)) để kiếm muối
            new_game = input("Bạn có muốn chơi lại để kiếm thêm chút muối không? Vui lòng ấn phím y: để tiếp tục cuộc vui; phím n: để kết thúc:  '")
            if new_game[0].lower() == 'y':
                playing = True
                continue
            else:
                print('Cám ơn bạn đã tham gia sòng bạc của chúng tôi ')

                break

# Let do it 
abc = Game()
abc.play()