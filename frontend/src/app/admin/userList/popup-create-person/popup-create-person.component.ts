import {Component, Inject} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {CheckEmailService} from "../../../common/services/checkEmail/check-email.service";
import {HashageService} from "../../../common/services/hashage/hashage.service";



@Component({
  selector: 'app-popup-create-person',
  templateUrl: './popup-create-person.component.html',
  styleUrls: ['./popup-create-person.component.scss']
})
export class PopupCreatePersonComponent
{
    person = {
        id: "",
        nickname: "",
        email: "",
        hash_pass: "",
        is_admin: false,
    };
    password: string = "";
    confirmPassword: string = "" ;
    changePassword: boolean = false ;
    hasError: boolean = false;
    errorMessage: string = "" ;


    constructor( public dialogRef: MatDialogRef<PopupCreatePersonComponent>,
                 @Inject(MAT_DIALOG_DATA) public data: any,
                 private checkEmailService: CheckEmailService,
                 private hashageService: HashageService ) { }


    // Appuie sur le bouton "valider"
    onValider(): void
    {
        this.checkField();
        if(!this.hasError)
        {
            if(this.changePassword) this.person.hash_pass = this.hashageService.run(this.password);
            const data = { user: this.person };

            // ...

            // Faux code
            this.onValiderCallback({ status: "success", data: {}});
        }
    }


    // Callback de 'onValider'
    onValiderCallback(retour: any)
    {
        if(retour.status === 'error')
        {
            console.log(retour);
            this.dialogRef.close(null);
        }
        else {
            this.dialogRef.close(this.person);
        }
    }


    // Check les champs saisis par l'utilisateur
    checkField(): void
    {
        if(this.person.nickname.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'pseudo'.";
            this.hasError = true;
        }
        else if(this.person.email.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'email'.";
            this.hasError = true;
        }
        else if(!this.checkEmailService.isValidEmail(this.person.email)) {
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
