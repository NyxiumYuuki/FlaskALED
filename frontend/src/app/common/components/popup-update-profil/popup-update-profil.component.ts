import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {CheckEmailService} from "../../services/checkEmail/check-email.service";
import {MessageService} from "../../services/message/message.service";



@Component({
  selector: 'app-popup-update-profil',
  templateUrl: './popup-update-profil.component.html',
  styleUrls: ['./popup-update-profil.component.scss']
})
export class PopupUpdateProfilComponent implements OnInit
{
    personCopy: any;
    newPassword: string = "";
    confirmNewPassword: string = "" ;
    changePassword: boolean = false ;
    hasError: boolean = false;
    errorMessage: string = "" ;


    constructor( private checkEmailService: CheckEmailService,
                 private messageService: MessageService,
                 public dialogRef: MatDialogRef<PopupUpdateProfilComponent>,
                 @Inject(MAT_DIALOG_DATA) public data: any ) { }


    ngOnInit(): void
    {
        const person = this.data.person;
        this.personCopy = {
            id: person.id,
            nickname: person.nickname,
            email: person.email,
            is_admin: person.is_admin
        };
    }


    // Appuie sur le bouton "valider"
    onValider(): void
    {
        this.checkField();
        if(!this.hasError)
        {
            let data: any = {nickname: this.personCopy.nickname};
            if(this.changePassword) data = {
                nickname: this.personCopy.nickname,
                password: this.newPassword
            };
            this.messageService
                .put("user/update", data)
                .subscribe(ret => this.onValiderCallback(ret), err => this.onValiderCallback(err));
        }
    }


    // Callback de 'onValider'
    onValiderCallback(retour: any)
    {
        if(retour.status === "success")
        {
            this.dialogRef.close(retour);
        }
        else if(retour.status === "error")
        {
            console.log(retour);
            this.errorMessage = retour.message;
            this.hasError = true;
        }
        else {
            console.log(retour);
            this.dialogRef.close(null);
        }
    }


    // Check les champs saisis par l'utilisateur
    checkField(): void
    {
        if(this.personCopy.nickname.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'pseudo'" ;
            this.hasError = true;
        }
        else if(this.personCopy.email.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'email'" ;
            this.hasError = true;
        }
        else if(!this.checkEmailService.isValidEmail(this.personCopy.email)) {
            this.errorMessage = "Email invalide" ;
            this.hasError = true;
        }
        else if((this.changePassword) && (this.newPassword.length === 0)) {
            this.errorMessage = "Veuillez remplir le champ 'mot de passe'";
            this.hasError = true;
        }
        else if((this.changePassword) && (this.newPassword !== this.confirmNewPassword)) {
            this.errorMessage = "Le mot de passe est différent de sa confirmation";
            this.hasError = true;
        }
        else {
            this.errorMessage = "" ;
            this.hasError = false;
        }
    }

}
