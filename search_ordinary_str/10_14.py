
class Solution():
    def commonChars(self, A):
        dictInList=[]
        for i in A:
            a=self.makeDict(i)
            dictInList.append(a)
        min_long_dict=self.searchMinLong(dictInList)
        #print(max_long_dict)
        target_dict={}
        for i,j in min_long_dict.items():
            min_num = int(1000000)
            for k in dictInList:
                if i in k:
                    num=k[i]
                    if int(num)<=min_num:
                        min_num=int(num)
                else:
                    break
                target_dict[i]=min_num
        output=self.transDictToList(target_dict)
        return output


    def transDictToList(self,target_dict):
        final_list=[]
        for i,j in target_dict.items():
            for k in range(int(j)):
                final_list.append(i)
        return final_list



    def makeDict(self, A_str):
        dict_str={}
        for idx,i in enumerate(A_str):
            if i in dict_str:
                dict_str[i]+=1
            else:
                dict_str[i]=1

        return dict_str

    def searchMinLong(self,dictInList):
        MinLength=100000
        for idx,i in enumerate(dictInList):
            length=len(i)
            if length <=MinLength:
                MinLength=length
                best_idx=idx

        return dictInList[best_idx]

if __name__=="__main__":
    a=["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
    solve=Solution()
    b=solve.commonChars(a)
    print(b)




