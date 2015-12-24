# -*- coding: utf-8 -*-


from __future__  import division
from datetime import datetime
from openerp import fields, models,api
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as OE_DFORMAT



#from openerp.addons.hr_payroll import hr_payslip as payslip


class hr_contract(models.Model):

    _inherit ='hr.contract'
    #_inherit='hr.payslip'

    worked_years = fields.Integer(String='Work Years', readonly=True, compute='_compute_working')
    increasing_percentage = fields.Float('annual increase persenage', readonly=False)
    current_year = fields.Integer(String='Current payslip year', readonly=True)
    current_month=fields.Integer(String='Current payslip month', readonly=True)
    wage=fields.Float('Wage', digits=(16,2), required=True, help="Basic Salary")
    #differ=fields.Integer(String='Differ',readonly=False,compute="calc_differ")
    is_updated=fields.Integer(String='is_updated',readonly=True,)
    last_wage=fields.Float('last salary ', digits=(16,2), readonly=True)
    difference_months=fields.Integer(String='difference_months', readonly=True)
    #difference_mon=fields.Integer(String='difference_mon', readonly=True,compute="calc_m")
    active_increase=fields.Boolean(string='Add Annual Salary Of The last_wagevious years')
    percent=fields.Float('percent', digits=(16,2), required=True,readonly=True)
    #newpercent=fields.Float('newpercent', digits=(16,2), required=True)
   # basic_wage=fields.Float('Basic_wage',readonly=True,value=wage)
    #determine=fields.Char(string='det',compute='select_det')



    @api.one
    def _compute_working(self):
        date_start = datetime.strptime(self.date_start, OE_DFORMAT).date()
        date_today = datetime.now().date()
        difference_years = date_today.year - date_start.year
        current_month=date_today.month
        start_working_month=date_start.month
        self.difference_months=current_month-start_working_month
        if self.difference_months>=0:
            self.worked_years=difference_years
        else:
            self.worked_years=(difference_years-1)

        return self.worked_years


    '''
    @api.one
    def _compute_working_months(self):
         date_today= datetime.strptime(self.datevar, OE_DFORMAT).date()
         self.current_year =self.datevar.year
         return self.current_year

    @api.one
    def _compute_pworking_monttemps(self):
        date_today= datetime.strptime(self.datevar, OE_DFORMAT).date()
        self.current_month =date_today.month
        return self.current_month
    '''
    def calc_wage(self,wage,dating,context=None):
            temp=self.wage
            self.current_year=datetime.strptime(dating, OE_DFORMAT).date().year
            self.current_month=datetime.strptime(dating, OE_DFORMAT).date().month
            date_start = datetime.strptime(self.date_start, OE_DFORMAT).date()
            current_month=self.current_month
            start_working_month=date_start.month
            difference_mon=current_month-start_working_month
            determine=str(self.active_increase)
            if self.is_updated==0:
              self.is_updated=datetime.strptime(self.date_start, OE_DFORMAT).date().year
            differ= self.current_year-self.is_updated
            if((differ>1 or((differ==1)and(difference_mon>=0)))and(determine=="False")):
                 differ=1
            if (difference_mon<0 and determine=="True"):
                differ=differ-1
            if self.current_year > datetime.now().date().year:
                for x in range(differ):
                    temp=temp+((temp*wage)/100)
                return temp
            elif self.current_year<datetime.now().date().year:
                if self.current_year>self.is_updated:
                    for x in range(differ):
                         temp=temp+((wage*temp)/100)
                    return temp
                elif self.current_year<self.is_updated:
                    self.percent=(wage/100)+(wage/wage)
                    newpercent=(1/self.percent)
                    newdiffer=(self.is_updated)-(self.current_year)
                    if self.current_month<start_working_month:
                        newdiffer=newdiffer+1
                    if(temp==(self.last_wage)+((self.last_wage*wage)/100)):
                        for x in range(newdiffer):
                            temp=temp*newpercent
                        return temp
                    else:
                        return self.last_wage
            else:
                  if differ!=0:
                        self.last_wage=self.wage
                  for x in range(differ):
                        self.wage=self.wage+((self.wage*wage)/100)
                  chek=self.wage-self.last_wage
                  if  chek>0:
                        self.is_updated=self.current_year
                  return self.wage

    '''
    def calc_differ(self):
        if self.is_updated==0:
        
            self.is_updated=datetime.strptime(self.date_start, OE_DFORMAT).date().year
        self.differ= self.current_year-self.is_updated
        #self.differ= datetime.now().date().year-self.is_updated
        if((self.differ!=0)and(self.determine=="False")):
            self.differ=1
        return self.differ


    def calc_m(self):
          date_start = datetime.strptime(self.date_start, OE_DFORMAT).date()
          current_month=self.current_month
          start_working_month=date_start.month
          self.difference_mon=current_month-start_working_month
          return self.difference_mon


    def  set_is_active(self):
        return True

    def select_det(self):
     self.determine=str(self.active)
     return self.determine
'''
    '''
     def _get_date_from(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        obj_contract = self.pool.get('hr.payslip')
        for emp in self.browse(cr, uid, ids, context=context):
            date_from = obj_contract.search(cr, uid,'employee_id','=',emp.id, context=context)
            if date_from:
                res[emp.id] =date_from[-1:][0]
            else:
                res[emp.id] = False
        return res




class hr_payslip(models.Model):
     _inherit ='hr.payslip'
     def _get_latest_contract(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        obj_contract = self.pool.get('hr.payslip')
        for emp in self.browse(cr, uid, ids, context=context):
            date_from = obj_contract.search(cr, uid,'employee_id','=',emp.id, context=context)
            if date_from:
                res[emp.id] =date_from[-1:][0]
            else:
                res[emp.id] = False
        return res
'''




