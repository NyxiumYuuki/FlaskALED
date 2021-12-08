import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {Person} from "../../../interfaces/Person";
import {CheckEmailService} from "../../../services/checkEmail/check-email.service";
import {HashageService} from "../../../services/hashage/hashage.service";



@Component({
  selector: 'app-popup-update-profil',
  templateUrl: './popup-update-profil.component.html',
  styleUrls: ['./popup-update-profil.component.scss']
})
export class PopupUpdateProfilComponent implements OnInit
{
    personCopy: Person;
    newPassword: string = "";
    confirmNewPassword: string = "" ;
    changePassword: boolean = false ;
    hasError: boolean = false;
    errorMessage: string = "" ;


    constructor( public dialogRef: MatDialogRef<PopupUpdateProfilComponent>,
                 @Inject(MAT_DIALOG_DATA) public data: any,
                 private checkEmailService: CheckEmailService,
                 private hashageService: HashageService ) { }


    ngOnInit(): void
    {
        const person = this.data.person;
        this.personCopy = {
            id: person.id,
            login: person.login,
            email: person.email,
            hashPass: person.hashPass,
            role: person.role
        };
    }


    // Appuie sur le bouton "valider"
    onValider(): void
    {
        this.checkField();
        if(!this.hasError)
        {
            if(this.changePassword) this.personCopy.hashPass = this.hashageService.run(this.newPassword);
            const data = { user: this.personCopy };

            // ...

            // Faux code
            this.onValiderCallback({ status: "success"});
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
        else
        {
            this.dialogRef.close(this.personCopy);
        }
    }


    // Check les champs saisis par l'utilisateur
    checkField(): void
    {
        if(this.personCopy.login.length === 0) {
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
