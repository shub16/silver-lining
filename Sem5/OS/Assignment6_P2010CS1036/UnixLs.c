#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/dir.h>
#include<sys/stat.h>
#include<sys/param.h>
#include<string.h>
#include<errno.h>
#include<pwd.h>
#include<grp.h>
#include<math.h>
#include<time.h>
#define FALSE 0
#define TRUE !FALSE
extern int alphasort();
char path[MAXPATHLEN];
void inode(char* fileName){
 
  struct stat buf;
  int ret = stat(fileName, &buf);
  ino_t inodeNum = buf.st_ino;
  
  printf("%lu ", inodeNum);
}
int file(const struct direct *entry){
    
  if((strcmp(entry->d_name,".")==0) || (strcmp(entry->d_name,"..")==0)){
    return FALSE;}
  else 
    return TRUE;
}
void get_size(struct stat buf){

  off_t fileSize = buf.st_size;
  printf("%5lu ",fileSize);
  return;
}
void nlink(struct stat buf){

  nlink_t numLink = buf.st_nlink;
  printf(" %1zu", numLink);
  return;
}
void info(struct stat buf){


  ushort mode = buf.st_mode;
  int ind;
  char *accesses[] = {"---","--x","-w-","-wx","r--","r-x","rw-","rwx"};
    
  for(ind = 6;ind >=0 ;ind -=3)
    printf("%s", accesses[(mode >> ind) & 7]);
  //printf("\n");
}
void get_time(struct stat buf){

  time_t lastModTime = buf.st_mtime;
  char* getLocalTime = ctime(&lastModTime);
  int ind;
  for(ind=4;ind<16;ind++){
    printf("%c",getLocalTime[ind]);
    }
  return;
}
char* get_gid(struct stat buf){

  struct group *grp=NULL;
  
  grp = getgrgid(buf.st_gid);
  
  if(grp!=NULL){
      
    return grp->gr_name;
    }
}
char* get_uid(struct stat buf){

  struct passwd *pw=NULL;
  pw = getpwuid(buf.st_uid);
  if(pw!=NULL)
    return pw->pw_name;
}
void file_info(char* fileName){
  struct stat buf;
  int ret = stat(fileName, &buf);
  
  if(S_ISDIR(buf.st_mode)) 
      printf("d");
  else
      printf("-");
  info(buf);
  nlink(buf);
  printf(" %s ",get_uid(buf));
  printf("%s ",get_gid(buf));
  get_size(buf);
  get_time(buf);
  printf("  %s ",fileName);
  printf("\n");
}
void print_name(char* fileName){
  printf("%-15s ",fileName);
}
void print_i(char* fileName){
  struct stat buf;
  int ret = stat(fileName, &buf);
  ino_t inodeNum = buf.st_ino;
  printf("%-6lu", inodeNum);
  printf(" %-14s ",fileName);//printf("\n");
}
int is_directory(char* fp){
  
    struct stat buf;
    int ret = stat(fp, &buf);
    return S_ISDIR(buf.st_mode);
}
void ls(char* fp,char* dotPath, int type){
  int count , ind;
  struct direct **files;
  int file();
  count = scandir(fp, &files, file, alphasort);
  if(count <=0){
    
    printf("No files in the directory \n");
    chdir("..");
    getwd(path);
    return;
  };
  getwd(path);
  for(ind=0;ind < count;++ind){
      if(type== -1 || type == 3){
        if((ind%5)==0) printf("\n");
        print_name(files[ind]->d_name);
      }
            
      if(type==1 || type == 6){
        if((ind%3)==0) printf("\n");
        print_i(files[ind]->d_name);
       }
       
      if(type==2 || type == 9 ){
       //printf(" total %d \n", count);
       file_info(files[ind]->d_name);
      }
      
      if(type==5 || type == 12){
      
       inode(files[ind]->d_name);
       file_info(files[ind]->d_name);
      }
  }
  
 
 if((type%3)==0){
  

  char str[MAXPATHLEN];

  char temp[MAXPATHLEN];
  strcpy(temp,dotPath);
  
  for(ind=0;ind < count;++ind){ 
      
      strcpy(dotPath,temp); 
      strcat(dotPath,"/");
       
      if(is_directory(files[ind]->d_name)){
      
      strcat(dotPath,files[ind]->d_name);   
      printf("\n\n%s :\n",dotPath);
      getwd(str);
      strcat(str,"/");
      strcat(str,files[ind]->d_name);
      chdir(str);
      ls(str,dotPath,type);
       };
   }
   chdir(".."); 
 } 
   printf("\n"); //flush buffer      
   getwd(path);
  return;      
}

int main(int argc, char* argv[]) {

 int t=-1,ex=0 ;
 char Path[4096];
 if(argc < 2){
  t = -1;
   
   strcpy(Path,".");
   strcpy(path,".");
   ls(path,Path,t);
   return 0;
  }
   if(argc>=2){ 
    if(strcmp(argv[1],"-i")==0) t = 1;
    else if(strcmp(argv[1],"-l")==0) t = 2;
    else if(strcmp(argv[1] ,"-R")==0) t = 3;
    else if(strcmp(argv[1],"-il")==0 || strcmp(argv[1],"-li")==0 ) t = 5;
    else if(strcmp(argv[1],"-iR")==0|| strcmp(argv[1],"-Ri")==0) t = 6;
    else if(strcmp(argv[1],"-lR")==0 || strcmp(argv[1],"-Rl")==0) t = 9;
    else if(strcmp(argv[1],"-ilR")==0|| strcmp(argv[1],"-iRl")==0 || strcmp(argv[1],"-Ril")==0 || strcmp(argv[1],"-Rli")==0 || strcmp(argv[1],"-liR")==0 || strcmp(argv[1],"-lRi")==0) t = 12;
    }
  if(t == -1 && argc ==2){ 
      strcpy(path,argv[1]);
      chdir(path);
      strcpy(Path,argv[1]);
      ls(path,Path,t);  
      return 0;    
    }
  if(t!=-1 && argc == 2){
   strcpy(Path,".");
   strcpy(path,".");
   if ((t%3)==0) printf(" %s : \n",path);
   ls(path,Path,t);
   return 0;
  }  
 if(argc>=3){
    int i,start;
    if(t==-1) start=1;
    else start=2;
    for(i=start;i<argc;i++){
      strcpy(path,argv[i]);
      chdir(path);
      if ((t%3)==0) printf(" %s : \n",path);
      printf(" %s \n",path);
      strcpy(Path,argv[i]);
      ls(path,Path,t);  
      getwd(path);
      chdir(path);
    }
   return 0;
 }
}
  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
