import {Component} from '@angular/core';
import {Router} from "@angular/router";
import {MessageService} from "../../common/services/message/message.service";
import {ProfilService} from "../../common/services/profil/profil.service";



@Component({
  selector: 'app-page-nickname',
  templateUrl: './page-login.component.html',
  styleUrls: ['./page-login.component.scss']
})
export class PageLoginComponent
{
    email: string = "" ;
    password: string = "" ;
    hasError: boolean = false;
    errorMessage: string = "";


    constructor( private messageService: MessageService,
                 private router: Router,
                 private profilService: ProfilService ) { }


    // Appuie sur le bouton "seConnecter"
    onSeConnecter(): void
    {
        this.checkField();
        if(!this.hasError)
        {
            const data = {
                email: this.email,
                password: this.password
            };
            this.messageService
                .post('login', data)
                .subscribe( retour => this.onSeConnecterCallback(retour), err => this.onSeConnecterCallback(err));
        }
    }


    // Callback de "onSeConnecter"
    onSeConnecterCallback(retour: any): void
    {
        if(retour.status !== "success")
        {
            console.log(retour);
            this.errorMessage = retour.error.message;
            this.hasError = true;
        }
        else {
            this.profilService.setId(retour.data.id);
            this.profilService.setIsAdmin(retour.data.is_admin)
            if(retour.data.is_admin) this.router.navigateByUrl('admin/userList');
            else this.router.navigateByUrl('user/registry');
        }
    }


    // Check les champs saisis par l'utilisateur
    checkField(): void
    {
        if(this.email === "") {
            this.errorMessage = "Veuillez remplir le champ email" ;
            this.hasError = true;
        }
        else if(this.password === "") {
            this.errorMessage = "Veuillez remplir le champ mot de passe" ;
            this.hasError = true;
        }
        else {
            this.errorMessage = "" ;
            this.hasError = false;
        }
    }

}
