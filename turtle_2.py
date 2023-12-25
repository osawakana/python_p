#turtleモジュールからカメオブジェクトをインポート 
from turtle import Turtle
#turtleモジュールから画面を表示させ続けるモジュールをインポート 
from turtle import done
#randomモジュールからランダムな整数を生成するモジュールをインポート
from random import randint
#カメオブジェクトを生成
tur = Turtle()
#カメの大きさを指定
tur.shapesize(2, 2)
#カメの形を指定
tur.shape("turtle")
#カメの色を指定
tur.color("cyan",'pink')


#実際の処理を行う関数(引数nにはn角形のnが入る)
def main(n):
    
    #n角形の外角をラムダ式で表す 360度周る
    ex_angle = lambda n: 360 / n
    #カメが実際に描く外角の計算をラムダ式ex_angleで求める
    tur_angle = ex_angle(n_poly)
    #n本の線を引くまで繰り返す 
    for i in range(n_poly):
        #カメ100px前へ進む
        tur.forward(100)
        #カメ左にtur_angle度曲がる
        tur.left(tur_angle)

#何角形か入力を受け取り整数値に型変換
n_poly = int(input("正何角形がいい?(数字は3以上にしてね!)"))

#3以上なら通常通りmain()の処理を行う

if n_poly >= 3:
    main(n_poly)

#それ以外なら例外だとわかるようにカメを怒らせる
else:
    #カメの注意喚起
    print("３以上って言ったじゃん!")
    #怒りの繰り返し
    for i in range(100):
        #怒りの値をランダムな整数として生成
        ang_num = randint(-100,100)
        #カメを赤色に染める
        tur.color("red")
        #カメを怒りの値分回転させる
        tur.left(ang_num)

#画面を表示し続ける関数
done()

