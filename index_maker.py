def CreateePresentIndex(self):
        
        techsortInd = self._dir + self._pathSep + self._TechsortProcessDir + self._pathSep + self._inFileName + self._indexFileExtn
        IndexFile   = open(self._dir + self._pathSep + self._ePresentDir + self._pathSep + self._outFileNameBase + ".pdf" + self._ep2indexFileExtn, "w")

#       get the current date 
        today = strftime("%Y-%m-%d")
        
#       create the index file
        StartPage = 1

        for line in csv.DictReader(open(techsortInd, "rb"), fieldnames=self._techsortFields, delimiter='\t'):
       
            if 'begin_doc' in str(line['MACRONAME']):

                PageCount = int(line["PAGECNT"])
                AcctNumberNodes = line['ACCOUNTNO'].split('-')
                
                AcctNumber =  AcctNumberNodes[0].strip() + AcctNumberNodes[1].strip() 
                LetterId   =  AcctNumberNodes[2].strip()

                UserdefNodes = line["USERDEF"].split('|')

                LetterDate  = UserdefNodes[0]
                CoMakerFlag = UserdefNodes[1]
                PrintFlag   = UserdefNodes[2]
  
                IndexRecord = AcctNumber + self._job + str(line['SEQUENCE']).rjust(6,"0") + "|" + str(AcctNumber) + "|" + str(LetterId) + "|" + str(LetterDate) + "|" + str(StartPage) + "|" + str(PageCount) + "|Statements|STMT|" + CoMakerFlag + '|' + PrintFlag
               
                IndexFile.write(IndexRecord + "\n")

                StartPage += PageCount
            
        IndexFile.close()
          