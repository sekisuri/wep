from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        print("Kiwoom 클래스")

        
        ## 변수모음
        self.account_num = None

        ####### event loop를 실행하기 위한 변수모음
       # self.login_event_loop = QEventLoop() #로그인 요청용 이벤트루프
       # self.detail_account_info_event_loop = QEventLoop() # 예수금 요청용 이벤트루프
       # self.calculator_event_loop = QEventLoop()
        self.login_event_loop = None
        self.detail_account_info_event_loop = None # 예수금 요청용 이벤트루프
        self.detail_account_info_event_loop2 = None # 예수금 요청용 이벤트루프
        #########################################
        self.get_ocx_instance()
        self.event_slots()
        self.signal_login_commConnect()
        self.get_account_info()
        self.detail_account_info()
        self.detail_account_mystock()

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot) # 로그인 관련 이벤트
        self.OnReceiveTrData.connect(self.trdata_slot) # 트랜잭션 요청 관련 이벤트
 #       self.OnReceiveMsg.connect(self.msg_slot)
    
    
    
    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect")

        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()
    
    def login_slot(self,errCode):
        print(errors(errCode))
        
        self.login_event_loop.exit()

    def get_account_info(self):
        account_list = self.dynamicCall("GetLoginInfo(QString)", "ACCNO") # 계좌번호 반환
        account_num = account_list.split(';')[0]

        self.account_num = account_num

        print("나의 보유 계좌번호 %s " % self.account_num)

        
    
    def detail_account_info(self):
        print("예수금 가져오는 부분")
        self.dynamicCall("SetInputValue(String,String","계좌번호",self.account_num)
        self.dynamicCall("SetInputValue(String,String","비밀번호","0000")
        self.dynamicCall("SetInputValue(String,String","비밀번호입력매체구분","00")
        self.dynamicCall("SetInputValue(String,String","조회구분","2")
        self.dynamicCall("CommRqData(String,String, int, String)","예수금상세현황요청","opw00001","0","2000")

        self.detail_account_info_event_loop = QEventLoop()
        self.detail_account_info_event_loop.exec_()
     
    def detail_account_mystock(self, sPrevNext = "0"):
        print("계좌평가 잔고내역 요청")       
        self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.account_num)
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호", "0000")
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호입력매체구분", "00")
        self.dynamicCall("SetInputValue(QString, QString)", "조회구분", "1")
        self.dynamicCall("CommRqData(QString, QString, int, QString)", "계좌평가잔고내역요청", "opw00018", sPrevNext, "2000")
        self.detail_account_info_event_loop2 = QEventLoop()
        self.detail_account_info_event_loop2.exec_()
    
    def trdata_slot(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext):
        '''
        sScrNo : 스크린번호 
        sRQName: 내가 요청했을 때 지은 이름
        sTrCode: 요청 id, tr코드
        sRecordName : 사용안함
        sPrevNext : 다음 페이지가 있는지
        '''

        if sRQName == "예수금상세현황요청":
            deposit = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "예수금")
            print("예수금 %s" % int(deposit))
            output_deposit = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "출금가능금액")
            print("출금가능금액 %s" % int(output_deposit))
            self.detail_account_info_event_loop.exit()
        
        elif sRQName == "계좌평가잔고내역요청":
            total_buy_money = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "총매입금액")
            self.total_buy_money = int(total_buy_money)
            print("총매입금액 %s" % self.total_buy_money)
            total_profit_loss_rate = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "총수익률(%)")
            total_profit_loss_rate_result = float(total_profit_loss_rate)
            print("총수익율 (%s) : %s" % ("%",total_profit_loss_rate_result))
            self.detail_account_info_event_loop2.exit()