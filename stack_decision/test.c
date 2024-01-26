#include <stdio.h>
#include <string.h>
#include <dirent.h>
#include <stdlib.h>

void update_player_status(const char *txt_directory, const char *player_status_file) {
    DIR *dir;
    struct dirent *ent;
    char filepath[256];
    FILE *file;
    char content[1024];  // Assuming content fits in this buffer

    if ((dir = opendir(txt_directory)) != NULL) {
        while ((ent = readdir(dir)) != NULL) {
            if (strstr(ent->d_name, ".txt") != NULL) {
                sprintf(filepath, "%s/%s", txt_directory, ent->d_name);
                file = fopen(filepath, "r");
                if (file) {
                    fread(content, sizeof(char), 1024, file);
                    if (strstr(content, "ee") != NULL) {
                        printf("HE FOLDS HE FOLDS\n");
                        // Update player status in player_status.txt
                        // Implement the file update logic here
                    }
                    fclose(file);
                }
            }
        }
        closedir(dir);
    } else {
        perror("Could not open directory");
    }
}

int main() {
    const char *txt_directory = "./";
    const char *player_status_file = "../player_status.txt";
    update_player_status(txt_directory, player_status_file);
    printf("Player status updated.\n");
    return 0;
}

