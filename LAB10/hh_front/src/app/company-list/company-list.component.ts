import {Component, OnInit} from '@angular/core';
import {Company} from "../company";
import {CompanyService} from "../company.service";

@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit{
  companies!: Company[];
  newCompany!: string;
  constructor(private companyService: CompanyService) {
  }
  ngOnInit() {
    this.companyService.getCompanies().subscribe((data) => {
      console.log(data);
      this.companies = data;
      })
  }
  addCompany(){
    this.companyService.createCompany(this.newCompany).subscribe((data)=>{
      console.log(data);
      this.companies.push(data);
      this.newCompany = "";
    })
  }



}
