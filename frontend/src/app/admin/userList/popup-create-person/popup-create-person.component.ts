import {Component, Inject} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {CheckEmailService} from "../../../common/services/checkEmail/check-email.service";
import {MessageService} from "../../../common/services/message/message.service";



@Component({
  selector: 'app-popup-create-person',
  templateUrl: './popup-create-person.component.html',
  styleUrls: ['./popup-create-person.component.scss']
})
export class PopupCreatePersonComponent
{
    nickname: string =  "";
    email: string = "";
    is_admin: boolean = false;
    password: string = "";

    confirmPassword: string = "" ;
    hasError: boolean = false;
    errorMessage: string = "" ;


    constructor( public dialogRef: MatDialogRef<PopupCreatePersonComponent>,
                 @Inject(MAT_DIALOG_DATA) public data: any,
                 private checkEmailService: CheckEmailService,
                 private messageService: MessageService ) { }


    // Appuie sur le bouton "valider"
    onValider(): void
    {
        this.checkField();
        if(!this.hasError)
        {
            const data = {
                email: this.email,
                nickname: this.nickname,
                password: this.password,
                is_admin: this.is_admin
            };
            this.messageService
                .post("admin/create/user", data)
                .subscribe(ret => this.onValiderCallback(ret), err => this.onValiderCallback(err));
        }
    }


    // Callback de 'onValider'
    onValiderCallback(retour: any)
    {
        if(retour.status !== 'success')
        {
            console.log(retour);
            this.errorMessage = retour.error.message;
            this.hasError = true;
        }
        else
        {
            this.dialogRef.close(retour);
        }
    }


    // Check les champs saisis par l'utilisateur
    checkField(): void
    {
        if(this.nickname.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'pseudo'.";
            this.hasError = true;
        }
        else if(this.email.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'email'.";
            this.hasError = true;
        }
        else if(!this.checkEmailService.isValidEmail(this.email)) {
            this.errorMessage = "Email invalide.";
            this.hasError = true;
        }
        else if(this.password.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'mot de passe'.";
            this.hasError = true;
        }
        else if(this.password !== this.confirmPassword) {
            this.errorMessage = "Le mot de passe est différent de sa confirmation.";
            this.hasError = true;
        }
        else {
            this.errorMessage = "" ;
            this.hasError = false;
        }
    }

}
