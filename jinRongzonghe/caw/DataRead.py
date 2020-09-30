'''
读文件的类
'''
import configparser
import os,yaml

class DataRead:
    def get_project_path(self):
        #获取当前工程路径
        current__file__path=os.path.realpath(__file__)

        dir_name=os.path.dirname(current__file__path)  #返回上一层目录
        dir_name = os.path.dirname(dir_name)
        return dir_name+"\\"

    def read_ini(self,file_path,key):
        '''
        读取ini文件，返回可以对应的value
        :param file_path: 文件路径
        :param key: key
        :return: key对应的value
        '''
        real_file_path=self.get_project_path()+file_path
        print(real_file_path)
        config=configparser.ConfigParser()
        config.read(real_file_path)  #读取ini配置文件
        value=config.get("env",key)  #读取[env]里面的key
        return value

    def read_yaml(self,file_path):
        '''
        读取yaml文件
        :param file_path:
        :return:  返回yaml的内容
        '''
        real_file_path=self.get_project_path()+file_path

        with open(real_file_path,"r",encoding='utf-8')as f:
            file_content=f.read()
            #yaml的load方法吧文本的内容转成字典的list
        content=yaml.load(file_content,Loader=yaml.FullLoader)
        return content


if __name__ == '__main__':
    #
    value=DataRead().read_ini(r"data_env\env.ini","url")
    print(value)
    list=DataRead().read_yaml(r"data_case\register_fail.yaml")
    print(list)

    list=DataRead().read_yaml(r"data_case\register_success.yaml")
    print(list)

    list = DataRead().read_yaml(r"data_case\register_repeat.yaml")
    print(list)

    list = DataRead().read_yaml(r"data_case\login_setup.yaml")
    print(list)

    list = DataRead().read_yaml(r"data_case\login_data.yaml")
    print(list)