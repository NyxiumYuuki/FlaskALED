import {Component} from '@angular/core';
import {Router} from "@angular/router";
import {MessageService} from "../../common/services/message/message.service";
import {HashageService} from "../../common/services/hashage/hashage.service";
import {environment} from "../../../environments/environment";



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
                 private hashageService: HashageService ) { }


    // Appuie sur le bouton "seConnecter"
    onSeConnecter(): void
    {
        console.log("test env: "+environment.api_url);
        this.checkField();
        if(!this.hasError)
        {
            let data = {
                email: this.email,
                hash_pass: this.hashageService.run(this.password)
            };
            console.log(data);
            /*
            this.messageService
                .sendMessage('user/auth', data)
                .subscribe( retour => this.callbackSeConnecter(retour))
            */
        }
    }


    // Callback de "onSeConnecter"
    callbackSeConnecter(retour: any): void
    {
        if(retour.status !== 200)
        {
            this.errorMessage = retour.error.data.reason;
            this.hasError = true;
        }
        else {
            //this.router.navigateByUrl( '/search' );
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
